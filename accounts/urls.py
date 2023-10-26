from django.urls import path
from accounts import views

urlpatterns = [
    
    
    path('login', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register', views.register, name='register'),
    path('profile_view/<int:id>/', views.profile_edit_view, name='profile_view'),
    
]