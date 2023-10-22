from django.urls import path
from accounts import views

urlpatterns = [
    
    
    path('accounts/login', views.loginView),
    
]