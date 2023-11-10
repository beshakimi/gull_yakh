from django.urls import path
from accounts import views

urlpatterns = [
    
    
    path('login', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register', views.register, name='register'),
    path('profile/<int:id>/', views.profile_edit_view, name='profile'),



    path('forget_password', views.forget_password_view, name='forget_password'),
    path('confirm_message', views.confirm_message_view, name='confirm_message'),
    # path('new_password', views.new_password_view, name='new_password'),
    path('confirm_change_password', views.confirm_change_password_view, name='confirm_change_password'),
    path('change_password', views.change_password_view, name='change_password'),

    # fore reset password in email link
    path('reset_password/<int:user_id>/<str:token>/', views.reset_password_confirm_view, name='reset_password_confirm'),

    

    




]