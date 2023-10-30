from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from persiantools.jdatetime import JalaliDate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from addProducts.models import foodModel
from addProducts.models import DringModel, Cart, CartItem, Checkout
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

def add_to_cart(request, id, model):
    if model == 'food':
        product_model = foodModel
    elif model == 'drink':
        product_model = DringModel
    else:
        return redirect('home')  # Invalid model provided

    product = product_model.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if product:
        if model == 'food':
            cart.food.add(product)
        elif model == 'drink':
            cart.drink.add(product)
        
        cart.save()
    else:
        return redirect('cart-detail')
    
    return redirect('cart-detail')

def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    foods = cart.food.all()
    drinks = cart.drink.all()
    
    return render(request, 'addProducts/shop_cart.html', {"cart": cart, "foods": foods, "drinks": drinks})


def create_cart_item(request, id):
    cart = Cart.objects.get(id=id)

    if request.method == 'POST':
       
        default_total_price = request.POST['default_total_price']
        print(default_total_price)
          

        cart_item = CartItem.objects.create(cart=cart, total_price=default_total_price)

        # Update the total price of the cart
        
        cart_item.save()

        return redirect('checkout', cart_item.id)


def create_checkout(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number1 = request.POST['phone_number1']
        phone_number2 = request.POST['phone_number2']
        tazkra_number = request.POST['tazkra_number']
        address = request.POST['address']
        
        checkout = Checkout.objects.get_or_create(
            user=request.user,
            cart_item=cart_item,
            name=name,
            email=email,
            phone_number1=phone_number1,
            phone_number2=phone_number2,
            tazkra_number=tazkra_number,
            address=address
        )
        checkout.save()
        
        # Redirect to a success page or perform further actions
        
    context = {
        'cart_item': cart_item,

    }
    return render(request, 'addProducts/user_info.html', context)