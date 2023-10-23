from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('addfood', views.create_food_model_view, name='create-food'),
    path('update-food/<int:food_id>/', views.update_food_model_view, name='update-food'),
    path('delete-food/<int:food_id>/', views.delete_food, name='delete-food'),
  
]