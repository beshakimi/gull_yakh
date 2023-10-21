from django.shortcuts import render
from django.http import HttpResponse
from persiantools.jdatetime import JalaliDate

from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel

# Create your views here.

# start home view 
def homeView(request):
    foods=foodModel.objects.all().order_by('-id')[:2]
    drink=DringModel.objects.all().order_by('-id')[:2]
    post=BlogModel.objects.all().order_by('-id')[:2]
    context={
            "foodlist":foods,
            "drinklist":drink,
            "postlist":post,
        }
    
    return render(request, "addProducts/home.html",context)

# start about view 
def aboutUsView(request):
    return render(request,"addProducts/about.html")


# food list view 
def foodListView(request):
    foods=foodModel.objects.all()
    context={
       "foodlist":foods,
       "foodcount":foods.count()
   }
    return render(request,"addProducts/foodList.html",context)
   
# food details view 
def foodDetailsView(request,food_id):
    food=foodModel.objects.get(pk=food_id)

    context={
      "foodDetails":food,  
    }

    return render(request,"addProducts/foodDetails.html",context, )

# drink list view
def drinkListView(request):
    drinks=DringModel.objects.all()
    context={
       "drinkList":drinks,
      #  "foodcount":foods.count()
   }
    return render(request,"addProducts/drinkList.html",context)
   

# drink detials view
def drinkDetailsView(request,drink_id):
    drink=DringModel.objects.get(pk=drink_id)

    context={
      "drinkDetails":drink,  
    }

    return render(request,"addProducts/drinkDetails.html",context )

# start blog view
def blogView(request):
    posts = BlogModel.objects.all()

    context={
        "postlist":posts,
    }

    return render(request,"addProducts/postList.html",context)

# start post details view
def postDetailsView(request,post_id):
    post=BlogModel.objects.get(pk=post_id)

    context={
        "postDetails":post,
    }
    return render(request,"addProducts/postDetails.html",context)

# start contacts view 
def contectView(request):
    return render(request,"addProducts/contacts.html")
