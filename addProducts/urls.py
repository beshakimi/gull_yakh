from django.urls import path
from addProducts import views

urlpatterns = [
    
    path('',views.homeView, name='home'),
    path('home', views.homeView),
    path('about' ,views.aboutUsView),
    path('food/list' ,views.foodListView),
    path('food/<int:food_id>' ,views.foodDetailsView),
    path('drink/list' ,views.drinkListView),
    path('drink/<int:drink_id>' ,views.drinkDetailsView ),
    path('blog/list' ,views.blogView),
    path('post/<int:post_id>',views.postDetailsView),
    path('contacts' ,views.contectView),
    path('shop_cart' ,views.shop_cart, name='shop_cart'),
    path('user_info' ,views.user_info, name='user_info'),
]