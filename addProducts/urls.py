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
    path('blog/list' ,views.blogView, name='post_list'),
    path('post/<int:post_id>',views.postDetailsView),
    path('contacts' ,views.contectView),
    path('shop_cart' ,views.shop_cart, name='shop_cart'),
    path('user_info' ,views.user_info, name='user_info'),
    # cart
    path('add-to-cart/<int:id>/<str:model>/', views.add_to_cart, name='add_to_cart'),
    path('cart-detail' ,views.view_cart, name='cart-detail'),
    path('cart-item/<int:id>' ,views.create_cart_item, name='cart-item'),
    path('checkout/<int:id>' ,views.create_checkout, name='checkout'),
    
    
]