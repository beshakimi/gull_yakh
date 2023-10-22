from django.urls import path
from addProducts import views

urlpatterns = [
    
    path('',views.homeView),
    path('addProduct/home', views.homeView),
    path('addProduct/about' ,views.aboutUsView),
    path('addProduct/food/list' ,views.foodListView),
    path('addProduct/food/<int:food_id>' ,views.foodDetailsView),
    path('addProduct/drink/list' ,views.drinkListView),
    path('addProduct/drink/<int:drink_id>' ,views.drinkDetailsView ),
    path('addProduct/blog/list' ,views.blogView),
    path('addProduct/post/<int:post_id>',views.postDetailsView),
    path('addProduct/contacts' ,views.contectView),
]