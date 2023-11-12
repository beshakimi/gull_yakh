from django.urls import path
from addProducts import views

urlpatterns = [
    
    path('',views.homeView, name='home'),
    path('home', views.homeView),

    # about
    path('about' ,views.aboutUsView, name='about'),

    # food

    path('food/list' ,views.foodListView, name='food'),
    path('food/<int:food_id>' ,views.foodDetailsView, name='food-detail'),

    # drink
    path('drink/list' ,views.drinkListView, name='drink'),
    path('drink/<int:drink_id>' ,views.drinkDetailsView, name='drink-detail' ),


    # blog
    path('blog/list' ,views.blogView, name='post_list'),
    path('post/<int:post_id>',views.postDetailsView, name='blog-detail'),

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
   

    path('checkout/<int:id>' ,views.create_checkout, name='checkout'),
    path('delete-cart/<int:id>' ,views.cart_delete, name='delete-cart'),

    # add comment
    path('add_food_comment/<int:pk>/', views.create_food_comment, name='add-food-comment'),
    path('add_drink_comment/<int:pk>/', views.create_drink_comment, name='add-drink-comment'),
    path('add_blog_comment/<int:pk>/', views.create_blog_comment, name='add-blog-comment'),
    path('add_website_comment/', views.create_website_comment, name='create-website-comment'),
    
    
    # delete comment
    path('delete_post_comment/<int:comment_id>/<int:post_id>/', views.delete_blog_comment, name="delete-post-comment"),
    path('delete_food_comment/<int:comment_id>/<int:food_id>/', views.delete_food_comment, name="delete-food-comment"),
    path('delete_drink_comment/<int:comment_id>/<int:drink_id>/', views.delete_drink_comment, name="delete-drink-comment"),


    

    
]