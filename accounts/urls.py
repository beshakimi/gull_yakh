from django.urls import path
from accounts import views

urlpatterns = [
    
    
    path('login', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register', views.register, name='register'),
    path('profile_view/<int:id>/', views.profile_edit_view, name='profile_view'),
    path('forget_password', views.forget_password_view, name='forget_password'),
    path('confirm_message', views.confirm_message_view, name='confirm_message'),
    path('new_password', views.new_password_view, name='new_password'),
    path('confirm_change_password', views.confirm_change_password_view, name='confirm_change_password'),
    path('change_password', views.change_password_view, name='change_password'),
    
]