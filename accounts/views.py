from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from accounts.models import User

# from .forms import MyPasswordChangeForm
from . import models
import uuid
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
import re


# Create your views here.
# def home(request):
#     return render(request, 'base.html')

# registeration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']



        if not re.match(r'^[a-zA-Z]{3}[a-zA-Z0-9_]*$', username):
            messages.error(request, "نام کاربری باید با حداقل سه حرف شروع شود و تنها شامل حروف انگلیسی، اعداد، و _ باشد")
            return redirect('register')
        
        if not re.match(r'^[a-zA-Z0-9]+@[a-zA-Z]{3,}.[a-zA-Z]{2,5}$', email):
            messages.error(request, "ایمیل آدرس اشباه است")
            return redirect('register')
        
        if len(password) < 1:
            messages.error(request, "پسورد باید بزرگتر از 6 حرف باشد")
            return redirect('register')

        if password != re_password:
            messages.error(request, "پسورد مطابقت ندارد.")
            return redirect('register')

        # if models.User.objects.filter(Q(email=email) & Q(email=email)).exists():
        #     messages.error(request, "کاربری با این نام موجود است")
        #     return redirect('register')

        if models.User.objects.filter(email=email).exists():
            messages.error(request, "کاربری با این ایمل موجود است ")
            return redirect('register')

        user = models.User.objects.create_user(username=username, email=email, password=password)
        
        user = user.save()
        

        messages.success(request, "حساب موفقانه ساخته شد")
        return redirect('login')

    return render(request, 'accounts/register.html')

# login view
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email:
            messages.error(request, " ایمیل خود را وارد کنید !")
            return redirect("login")

        if not password:
            messages.error(request, "پسورد خود را وارد کنید!")
            return render(request, "accounts/login.html")

        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "کاربر با این مشخصات یافت نشد!!")
            return render(request, "accounts/login.html")
        
        login(request, user) 

        return redirect("home")

    return render(request, "accounts/login.html")

# logout view 
def logout_page(request):
    logout(request)
    return redirect("login")
 

# profile edit view
def profile_edit_view(request, id):
    profile = get_object_or_404(Profile, pk=id)
    user = request.user
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']
        
        gender = request.POST.get('gender', profile.gender)
        
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            profile.avatar = avatar

        profile.first_name =first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.gender = gender
        profile.user = user
      
        
        profile.save()
        
        return redirect('home')
    else:
        return render(request, 'accounts/profile.html', {'profile': profile, 'user': user})
    

# forget password view 
def forget_password_view(request):
     
    return render(request, "accounts/forget_password.html")


#  confirm message view 
def confirm_message_view(request):
    return render(request, "accounts/confirm_message.html")

# # forget new password view 
def new_password_view(request):
    return render(request, "accounts/new_password.html")

# # new password view 
def confirm_change_password_view(request):
    return render(request, "accounts/confirm_change_password.html")

# change password view 
@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # بررسی صحت رمز عبور قبلی
        if request.user.check_password(old_password):
            # بررسی تطابق رمز عبور جدید
            if new_password1 == new_password2:
                # تغییر رمز عبور
                request.user.set_password(new_password1)
                request.user.save()
                redirect('confirm_message')

                update_session_auth_hash(request, request.user)  # رفع خطر از دست دادن جلسه ورود
                messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد.')
                return redirect('confirm_change_password')  # تغییر مسیر به جایی که دلخواهید
            else:
                messages.error(request, 'رمز عبور جدید با تایید رمز عبور مطابقت ندارد.')
        else:
            messages.error(request, 'رمز عبور فعلی اشتباه است.')
    
    return render(request, "accounts/change_password.html")



    







