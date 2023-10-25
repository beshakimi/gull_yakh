from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
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
        
        if len(password) < 6:
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
        user.save()

        messages.success(request, "حساب موفقانه ساخته شد")
        return redirect('login')

    return render(request, 'accounts/register.html')

# login page view
def login_page(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if not email:
            messages.error(request, " ایمیل خود را وارد کنید !")
            return redirect("login")

        if not password:
            messages.error(request, "پسورد خود را وارد کنید!")
            return render(request, "accounts/login.html")

        try:
             user = models.User.objects.get(Q(email=email) & Q(password=password))
        except models.User.DoesNotExist:
            messages.error(request, "کاربر با این مشخصات یافت نشد!!")
            return render(request, "accounts/login.html")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "ایمیل یا پسورد اشتباه است")
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")

# def login_page(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]

#         try:
#             user = models.User.objects.get(email=email)

#         except:
#             messages.error(request, "کاربر با این مشخصاب موجود نمی باشد")
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)

#             return redirect("home")
#         else:
#             messages.error(request, "ایمل یا پسورد اشتباه است")

#     return render(request, "accounts/login.html")

login_required(login_url="login")
def logout_page(request):
    logout(request)
    return redirect("login")
