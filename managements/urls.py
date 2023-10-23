from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboar_view, name='dashboard'),
    path('addfood', views.create_food_model_view, name='create-food'),
    path('update-food/<int:food_id>/', views.update_food_model_view, name='update-food'),
    path('delete-food/<int:food_id>/', views.delete_food, name='delete-food'),
    path('addDrink', views.create_drink_model_view, name='create-drink'),
    path('update-drink/<int:drink_id>/', views.update_drink_model_view, name='update-drink'),
    path('delete-drink/<int:drink_id>/', views.delete_drink, name='delete-drink'),
  
]