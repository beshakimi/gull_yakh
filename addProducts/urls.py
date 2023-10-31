from django.urls import path
from addProducts import views

urlpatterns = [
    
    path('',views.homeView, name='home'),
    path('home', views.homeView),

    # about
    path('about' ,views.aboutUsView),

    # food
    path('food/list' ,views.foodListView),
    path('food/<int:food_id>' ,views.foodDetailsView),

    # drink
    path('drink/list' ,views.drinkListView),
    path('drink/<int:drink_id>' ,views.drinkDetailsView ),

    # blog
    path('blog/list' ,views.blogView, name='post_list'),
    path('post/<int:post_id>',views.postDetailsView),

    # contact
    path('contacts' ,views.contectView),

    # shop_cart
    path('shop_cart' ,views.shop_cart, name='shop_cart'),
    path('user_info' ,views.user_info, name='user_info'),

    # cart
    path('add-to-cart/<int:id>/<str:model>/', views.add_to_cart, name='add_to_cart'),
    path('cart-detail' ,views.view_cart, name='cart-detail'),
    path('cart-item/<int:id>' ,views.create_cart_item, name='cart-item'),


    # search
    path('search_result' ,views.search_result_view, name='search_result'),
   
    
]