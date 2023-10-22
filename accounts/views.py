from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import addProducts

# Create your views here.
def loginView(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse(addProducts.views.homeView))
            pass
        else:
            context={
                'email':email,
                'errorMessage':"شخصی با این ایمل یافت نشد",
            }
            pass
    else:
        return render(request, "accounts/login.html")