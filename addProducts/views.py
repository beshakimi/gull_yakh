from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from persiantools.jdatetime import JalaliDate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel
from accounts.models import Profile

# Create your views here.

# start home view 
def homeView(request):
    foods=foodModel.objects.all().order_by('-id')[:8]
    drink=DringModel.objects.all().order_by('-id')[:8]
    post=BlogModel.objects.all().order_by('-id')[:4]
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
    foods=foodModel.objects.all().order_by('-id')
    page = request.GET.get('page')

    # تعداد نوشیدنی‌ها در هر صفحه
    items_per_page = 8

    paginator = Paginator(foods, items_per_page)
    try:
        foods = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        foods = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        foods = paginator.page(page)
    
    left_index = (int(page) - 2 )
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    pagination_range = range(left_index, right_index + 1)
    context={
       "foodlist":foods,
       "pagination_range": pagination_range,
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
    # دریافت همه نوشیدنی‌ها
    drinks = DringModel.objects.all().order_by('-id')
    page = request.GET.get('page')

    # تعداد نوشیدنی‌ها در هر صفحه
    items_per_page = 8

    paginator = Paginator(drinks, items_per_page)
    try:
        drinks = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        drinks = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        drinks = paginator.page(page)
    
    left_index = (int(page) - 2 )
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    pagination_range = range(left_index, right_index + 1)

    context = {
        'drinkList': drinks,
        'pagination_range': pagination_range,
    }

    return render(request, 'addProducts/drinkList.html', context)

   

# drink detials view
def drinkDetailsView(request,drink_id):
    drink=DringModel.objects.get(pk=drink_id)

    context={
      "drinkDetails":drink,  
    }

    return render(request,"addProducts/drinkDetails.html",context )

# start post list view
def blogView(request):
    posts = BlogModel.objects.all().order_by('-id')

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

def profile_view(request, id):
    profile = get_object_or_404(Profile, pk=id)
    user = request.user
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']
        
        
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            profile.avatar = avatar

        profile.first_name =first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.gender = gender
        profile.user = user
      
        
        profile.save()
        
        return redirect('home')
    else:
        return render(request, 'addProducts/profile.html', {'profile': profile, 'user': user})
    