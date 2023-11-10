from django.shortcuts import render,redirect,get_object_or_404,Http404
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
from accounts.models import User
from accounts import models

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import redirect
import re
from django.db.models import Q

# for sent email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# register view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']


        if not re.match(r'^[a-zA-Zآ-ی]{3}[a-zA-Z0-9_آ-ی]*$', username):
            messages.error(request, "نام نامعتبر است")
            return redirect('register')
        
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_.]*@[a-zA-Z]{3,}\.[a-zA-Z]{2,5}$', email):
            messages.error(request, "ایمیل آدرس نامتعبر است")
            return redirect('register')
        
        if len(password) < 6:
            messages.error(request, "پسورد باید بزرگتر از 6 حرف باشد")
            return redirect('register')

        if password != re_password:
            messages.error(request, "پسورد مطابقت ندارد.")
            return redirect('register')

        if models.User.objects.filter(Q(email=email) & Q(email=email)).exists():
            messages.error(request, "کاربری با این مشخصات موجود است")
            return redirect('register')

        # if models.User.objects.filter(email=email).exists():
        #     messages.error(request, "کاربری با این ایمل موجود است ")
        #     return redirect('register')

        user = models.User.objects.create_user(username=username, email=email, password=password)
        
        user = user.save()
        

        messages.success(request, "حساب موفقانه ساخته شد")
        return redirect('login')

    return render(request, 'accounts/register.html')

# login view 
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
        
        # بررسی نام و نام خانوادگی
        name_pattern = r'^[a-zA-Z_ ]+$'
        if not re.match(name_pattern, first_name): 
            # نام و نام خانوادگی باید فقط شامل حروف انگلیسی و سمبل '_' باشند
            messages.error(request, "نام نامعتبر است")
            return redirect('profile', id=profile.id)
        if not re.match(name_pattern, last_name):
            messages.error(request, "نام خانوادگی نامعتبر است")
            return redirect('profile', id=profile.id)
        
        # بررسی شماره تماس
        phone_pattern = r'^93\d{9}$'
        if not re.match(phone_pattern, phone):
            # شماره تماس باید 9 رقم و فقط شامل اعداد باشد
            messages.error(request, "شماره تماس باید با کد 93 شروع شود ")
            return redirect('profile', id=profile.id)
        
        # ادامه کدهای دیگر...
        
        import imghdr

        def validate_image_format(image):
            valid_formats = ('jpeg', 'jpg', 'png', 'gif', 'svg', 'webp')
            image_format = imghdr.what(image)
            if image_format not in valid_formats:
                raise ValidationError('فرمت عکس نامعتبر است.')

        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
        try:
            validate_image_format(avatar)
            profile.avatar = avatar
        except ValidationError as e:
            messages.error(request, str(e).strip('[]'))
            return redirect('profile', id=profile.id)
        # if 'avatar' in request.FILES:
        #     avatar = request.FILES['avatar']
        #     profile.avatar = avatar

        profile.first_name = first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.gender = gender
        profile.user = user

        profile.save()

        return redirect('home')
    else:
        return render(request, 'accounts/profile.html', {'profile': profile, 'user': user})
# def profile_edit_view(request, id):
#     profile = get_object_or_404(Profile, pk=id)
#     user = request.user
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         phone = request.POST['phone']
#         gender = request.POST['gender']
        
#         gender = request.POST.get('gender', profile.gender)
        
#         if 'avatar' in request.FILES:
#             avatar = request.FILES['avatar']
#             profile.avatar = avatar

#         profile.first_name =first_name
#         profile.last_name = last_name
#         profile.phone = phone
#         profile.gender = gender
#         profile.user = user
      
        
#         profile.save()
        
#         return redirect('home')
#     else:
#         return render(request, 'accounts/profile.html', {'profile': profile, 'user': user})
    

def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # اگر کاربری با این ایمیل وجود نداشته باشد
            return redirect('forget_password')  # یا به صفحه دیگری هدایت کنید

        # ایجاد توکن تصادفی برای بازنشانی پسورد
        token = default_token_generator.make_token(user)
        # ارسال لینک بازنشانی پسورد به ایمیل کاربر
        reset_link = request.build_absolute_uri(f'/accounts/reset_password/{user.pk}/{token}/')  # ساخت لینک بازنشانی پسورد
        
        # حذف تگ‌های HTML و نمایش متن
        email_text = strip_tags(render_to_string('accounts/reset_password_email.html', {'reset_link': reset_link}))

        send_mail(
            'Password Reset',
            email_text,
            'your_email@example.com',
            [email],
            fail_silently=False,
        )
        return redirect('confirm_message')  # یا به صفحه دیگری هدایت کنید
    else:
        return render(request, "accounts/forget_password.html")
    


    

    # برای اینکه وقتی بالای لینک کلیک شد به این صفحه راجع شود


def reset_password_confirm_view(request, user_id, token):
    if request.method == 'POST':
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if new_password1 == new_password2:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                # کاربری با این شناسه وجود ندارد
                raise Http404()

            if default_token_generator.check_token(user, token):
                # تغییر رمز عبور
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # رفع خطر از دست دادن جلسه ورود
                return redirect('confirm_change_password')  # تغییر مسیر به جایی که دلخواهید
            else:
                # توکن معتبر نیست
                raise Http404()
        else:
            messages.error(request, 'رمز عبور جدید با تایید رمز عبور مطابقت ندارد.')

    return render(request, 'accounts/new_password.html')

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
                return redirect('confirm_change_password')  # تغییر مسیر به جایی که دلخواهید
            else:
                messages.error(request, 'رمز عبور جدید با تایید رمز عبور مطابقت ندارد.')
        else:
            messages.error(request, 'رمز عبور فعلی اشتباه است.')
    
    return render(request, "accounts/change_password.html")



    







