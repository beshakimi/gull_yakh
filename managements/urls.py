from django.urls import path
from . import views

urlpatterns = [
    # food urls
    path('dashboard/', views.dashboar_view, name='dashboard'),
    path('addfood', views.create_food_model_view, name='create-food'),
    path('update-food/<int:food_id>/', views.update_food_model_view, name='update-food'),
    path('delete-food/<int:food_id>/', views.delete_food, name='delete-food'),

    # drink urls
    path('addDrink', views.create_drink_view, name='create-drink'),
    path('update-drink/<int:drink_id>/', views.update_drink_model_view, name='update-drink'),
    path('delete-drink/<int:drink_id>/', views.delete_drink, name='delete-drink'),

    # post urls
    path('addPost', views.create_post_view, name='create-post'),
    path('update-post/<int:post_id>/', views.update_post_view, name='update-post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete-post'),

    # user_list url
    path('user_list', views.user_list_view, name='user-list'),
    path('user_details/<int:id>', views.user_details, name='user-details'),

    # user_type
    path('admin_users', views.admin_users, name='admin_users'),
    path('users', views.users, name='users'),
]