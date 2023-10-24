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

# Create your views here.
# def home(request):
#     return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password != re_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if models.User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if models.User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # if not re.match(r'^[a-zA-Z0-9]+$', username):
        #     messages.error(request, "Username can only contain alphanumeric characters")
        #     return redirect('register')

        # if not re.match(r'^[a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', email):
        #     messages.error(request, "Invalid email address.")
        #     return redirect('register')

        if len(password) < 6:
            messages.error(request, "Password should be at least 8 characters long.")
            return redirect('register')


        user = models.User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')

    return render(request, 'accounts/register.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = models.User.objects.get(email=email)

        except:
            messages.error(request, "user does not exist!!!")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            return redirect("index")
        else:
            messages.error(request, "incorrect email or password")

    return render(request, "accounts/login.html")

login_required(login_url="login")
def logout_page(request):
    logout(request)
    return redirect("login")
