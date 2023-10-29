from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from persiantools.jdatetime import JalaliDate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from addProducts.models import foodModel
from addProducts.models import DringModel, Cart
from addProducts.models import BlogModel
from accounts.models import Profile

# Create your views here.

# start home view 
def homeView(request):
    user = request.user
    foods=foodModel.objects.all().order_by('-id')[:8]
    drink=DringModel.objects.all().order_by('-id')[:8]
    post=BlogModel.objects.all().order_by('-id')[:4]
    context={
            "foodlist":foods,
            "drinklist":drink,
            "postlist":post,
            'user': user,
            'section':'home'
        }
    
    return render(request, "addProducts/home.html",context)

# start about view 
def aboutUsView(request):
    context ={
        'section':'about'
    }
    return render(request,"addProducts/about.html", context)


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
       "section":"food"
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
        'section':'drink'
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
        'section':'blog',
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
    return render(request,"addProducts/contacts.html", {'section':'contact'})

# start shopping cart 
def shop_cart(request):
    return render(request,"addProducts/shop_cart.html")


# user information for order view
def user_info(request):
    return render(request,"addProducts/user_info.html")

# def add_to_cart(request):
#     if request.method == 'POST':
#         # Optional: If you want to use a form for adding items to the cart, create an instance of the form
#         form = AddToCartForm(request.POST)  # Replace AddToCartForm with your actual form class

#         if form.is_valid():
#             # Get the selected food and drink items from the form
#             food_items = form.cleaned_data['food']
#             drink_items = form.cleaned_data['drink']

#             # Create a new instance of the Cart model
#             cart = Cart.objects.create()

#             # Add the food and drink items to the cart
#             cart.food.set(food_items)
#             cart.drink.set(drink_items)


def add_to_cart(request, id):  
    product = foodModel.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if product:
        cart.food.add(product)
        cart.save()
    else:
        return redirect('cart-detail')
        
    return redirect('cart-detail')

def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    foods = cart.food.all()
    drinks = cart.drink.all()
    
    return render(request, 'addProducts/shop_cart.html', {"cart": cart, "foods": foods, "drinks": drinks})