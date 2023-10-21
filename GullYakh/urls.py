"""
URL configuration for GullYakh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from addProducts.views import homeView
from addProducts.views import aboutUsView
from addProducts.views import foodListView
from addProducts.views import foodDetailsView
from addProducts.views import drinkListView
from addProducts.views import drinkDetailsView
from addProducts.views import contectView
from addProducts.views import blogView
from addProducts.views import postDetailsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('addProduct/home', homeView),
    path('addProduct/about' ,aboutUsView),
    path('addProduct/food/list' ,foodListView),
    path('addProduct/food/<int:food_id>' ,foodDetailsView),
    path('addProduct/drink/list' ,drinkListView),
    path('addProduct/drink/<int:drink_id>' ,drinkDetailsView ),
    path('addProduct/blog/list' ,blogView),
    path('addProduct/post/<int:post_id>',postDetailsView),
    path('addProduct/contacts' ,contectView),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)