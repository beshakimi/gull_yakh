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
    path('profile_view/<int:id>/', views.profile_view, name='profile_view'),
    path('contacts' ,views.contectView),
]