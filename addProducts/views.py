from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from persiantools.jdatetime import JalaliDate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from addProducts.models import foodModel
from addProducts.models import DringModel, Cart, CartItem, Checkout, FoodComment, DrinkComment, BlogComment, WebsiteComment

from addProducts.models import BlogModel
from accounts.models import Profile

from django.db.models import Q
from django.contrib import messages

import random

from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required

# Create your views here.

# start home view 
def homeView(request):
    # add search functionality with js:
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)

    # send random comments to home:
    comments = WebsiteComment.objects.all()
    comment = None
    if comments:
        random_number = random.randint(0, len(comments)-1)
        comment = comments[random_number]
     
    
    # cart_item_count = request.user.cart.cartitem_set.filter(checked=False).count()
    user = request.user
    foods=foodModel.objects.all().order_by('-id')[:8]
    drink=DringModel.objects.all().order_by('-id')[:8]
    post=BlogModel.objects.all().order_by('-id')[:4]
    context={
            "foodlist":foods,
            "drinklist":drink,
            "postlist":post,
            "comment": comment,
            'user': user,
            'food_and_drink': food_and_drink,
            # 'cart_item_count': cart_item_count,
            'section':'home'
        }
    
    return render(request, "addProducts/home.html",context)

# start about view 
def aboutUsView(request):
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)
    
    context ={
        'section':'about',
        'food_and_drink': food_and_drink,
    }
    return render(request,"addProducts/about.html", context)


# food list view 
def foodListView(request):
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)

    foods=foodModel.objects.all().order_by('-id')
    page = request.GET.get('page')

    if request.method == 'POST':
        if 'name_checkbox' in request.POST:
            foods = foods.order_by('Title')  

        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price and max_price:
            foods = foods.filter(Price__range=(min_price, max_price))
    
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
       'food_and_drink': food_and_drink,
       "section":"food"
   }
    return render(request,"addProducts/foodList.html",context)
   

# food details view 
@login_required(login_url='login')
def foodDetailsView(request,food_id):
    food=get_object_or_404(foodModel,pk=food_id)
    comments = food.foodcomment_set.all().order_by('-id')

    context={
      "foodDetails":food,  
      "comments": comments,
      "section":"food"
    }

    return render(request,"addProducts/foodDetails.html",context, )

# drink list view
def drinkListView(request):
    # دریافت همه نوشیدنی‌ها
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)

    drinks = DringModel.objects.all().order_by('-id')
    page = request.GET.get('page')

    if request.method == 'POST':
        if 'name_checkbox' in request.POST:
            drinks = drinks.order_by('Title')  

        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price and max_price:
            drinks = drinks.filter(Price__range=(min_price, max_price))
    

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
         'food_and_drink': food_and_drink,
        'section':'drink'
    }

    return render(request, 'addProducts/drinkList.html', context)

   
# drink detials view
@login_required(login_url='login')
def drinkDetailsView(request,drink_id):
    drink=DringModel.objects.get(pk=drink_id)
    comments = drink.drinkcomment_set.all().order_by('-id')
    context={
      "drinkDetails":drink,  
      "comments": comments,
      "section":"drink"
    }

    return render(request,"addProducts/drinkDetails.html",context )

# start post list view
def blogView(request):
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)

    posts = BlogModel.objects.all().order_by('-id')
    page = request.GET.get('page')

        # تعداد نوشیدنی‌ها در هر صفحه
    items_per_page = 8

    paginator = Paginator(posts, items_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)
    
    left_index = (int(page) - 2 )
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    pagination_range = range(left_index, right_index + 1)

    context={
        "postlist":posts,
        'pagination_range': pagination_range,
        'food_and_drink': food_and_drink,
        'section':'blog',
    }

    return render(request,"addProducts/postList.html",context)

# start post details view
def postDetailsView(request,post_id):
    post=BlogModel.objects.get(pk=post_id)
    comments = post.blogcomment_set.all().order_by('-id')

    context={
        "postDetails":post,
        "comments": comments,
        "section":"blog"
    }
    return render(request,"addProducts/postDetails.html",context)

# start contacts view 
def contectView(request):
    food_and_drink = []
    for item in foodModel.objects.all():
        food_and_drink.append(item.Title)
    for item in DringModel.objects.all():
        food_and_drink.append(item.Title)
    context ={
        'section':'contact',
        'food_and_drink': food_and_drink,
    }
    return render(request,"addProducts/contacts.html", context )

# start shopping cart
@login_required(login_url='login')

def shop_cart(request):
    return render(request,"addProducts/shop_cart.html")


# user information for order view
def user_info(request):
    return render(request,"addProducts/user_info.html")

# add_to_cart view
@login_required(login_url='login')

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
            try:
                cart_item = CartItem.objects.get(Q(food=product) & Q(checked=False))
                cart_item.quantity += 1
                cart_item.total_price = str(cart_item.quantity * float(cart_item.total_price))
                cart_item.save()
            except:
                cart_item = CartItem.objects.create(
                    cart = cart, 
                    food = product,
                    quantity = 1,
                    total_price = product.Price,
                )
                
            
        elif model == 'drink':
            try:
                cart_item = CartItem.objects.get(Q(drink=product) & Q(checked=False))
                cart_item.quantity += 1
                cart_item.total_price = str(cart_item.quantity * float(cart_item.total_price))
                cart_item.save()
            except:
                cart_item = CartItem.objects.create(
                    cart = cart,
                    drink = product, 
                    quantity = 1, 
                    total_price = product.Price
                )
                
            
        
    else:
        return redirect('cart-detail')
    
    return redirect('cart-detail')

# view cart
@login_required(login_url='login')

def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.filter(
        Q(active=True) &
        Q(checked=False))
    
    
    return render(request, 'addProducts/shop_cart.html', {"cart": cart, "cart_items": cart_items})

# cart details view
@login_required(login_url='login')

def cart_delete(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    return redirect('cart-detail')  
    
    
    return redirect('cart-detail')

# cart item view
@login_required(login_url='login')

def create_cart_item(request, id):
    cart = Cart.objects.get(id=id)

    if request.method == 'POST':
       pass
    #     default_total_price = request.POST['default_total_price']
    #     print(default_total_price)
          

    #     cart_item = CartItem.objects.create(cart=cart, total_price=default_total_price)

    #     # Update the total price of the cart
        
    #     cart_item.save()
    
    return redirect('checkout', cart.id)

# chackout view
@login_required(login_url='login')  
def create_checkout(request, id):
    cart = get_object_or_404(Cart, id=id)
    total_price = 0
    for item in request.user.cart.cartitem_set.filter(checked = False):
        total_price += float(item.total_price)
    print(total_price)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number1 = request.POST['phone_number1']
        phone_number2 = request.POST['phone_number2']
        # tazkra_number = request.POST['tazkra_number']
        address = request.POST['address']
        
        checkout, created = Checkout.objects.get_or_create(
            user=request.user,
            cart=cart,
            name=name,
            email=email,
            phone_number1=phone_number1,
            phone_number2=phone_number2,
            # tazkra_number=tazkra_number,
            address=address, 
            
        )
        
        for item in request.user.cart.cartitem_set.filter(checked = False):
            item.checkout = checkout
            item.active = False
            item.save()
        messages.success(request, 'سفارش شما موفقانه ثبت گردید')
        return redirect('home')
       
        
        # Redirect to a success page or perform further actions
    cart_item = cart.cartitem_set.filter(checked = False)
    context = {
        'cart_item': cart_item,
        'total_price': total_price
         }
    return render(request, 'addProducts/user_info.html', context)


# search_result_view view
def search_result_view(request):
    query = request.GET.get('query')
    if query:
        food_results = foodModel.objects.filter(Q(Title__icontains=query))
        drink_results = DringModel.objects.filter(Q(Title__icontains=query))
        # food_results = foodModel.objects.filter(Q(Title__icontains=query) | Q(Category__icontains=query))
        # drink_results = DringModel.objects.filter(Q(Title__icontains=query) | Q(Category__icontains=query))
    else:
        food_results = []
        drink_results = []

    context = {
        'query': query,
        'food_results': food_results,
        'drink_results': drink_results,
    }

    return render(request, 'addProducts/search_result.html', context)

# create_food_comment view
@login_required(login_url='login')
def create_food_comment(request, pk):
    food = get_object_or_404(foodModel, id = pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        food_comment = FoodComment.objects.create(
            profile = request.user.profile, 
            food = food, 
            comment = comment
        )
        messages.success(request, "نظر با موفقیت اضافه شد.")
    return redirect('food-detail', pk)

# create_drink_comment view
@login_required(login_url='login')
def create_drink_comment(request, pk):
    drink = get_object_or_404(DringModel, id = pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        drink_comment = DrinkComment.objects.create(
            profile = request.user.profile, 
            drink = drink, 
            comment = comment
        )
        messages.success(request, "نظر با موفقیت اضافه شد.")
    return redirect('drink-detail', pk)

# create_blog_comment view
@login_required(login_url='login')
def create_blog_comment(request, pk):
    post = get_object_or_404(BlogModel, id = pk)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        blog_comment = BlogComment.objects.create(
            profile = request.user.profile, 
            post = post, 
            comment = comment
        )
        messages.success(request, "نظر با موفقیت اضافه شد.")
    return redirect('blog-detail', pk)

# create_website_comment view
@login_required(login_url='login') 
def create_website_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        website_comment = WebsiteComment.objects.create(
            profile = request.user.profile,  
            comment = comment
        )
        messages.success(request, "نظر با موفقیت اضافه شد.")
    return redirect('home')

# delete_blog_comment view 
def delete_blog_comment(request, comment_id, post_id ):
    post_comment = get_object_or_404(BlogComment, id=comment_id)
    post_comment.delete()
    messages.success(request, "نظر با موفقیت حذف شد.")
    return redirect('blog-detail', post_id)

# delete_food_comment view 
def delete_food_comment(request, comment_id, food_id ):
    food_comment = get_object_or_404(FoodComment, id=comment_id)
    food_comment.delete()
    messages.success(request, "نظر با موفقیت حذف شد.")
    return redirect('food-detail', food_id)

# delete_drink_comment view 
def delete_drink_comment(request, comment_id, drink_id ):
    drink_comment = get_object_or_404(DrinkComment, id=comment_id)
    drink_comment.delete()
    messages.success(request, "نظر با موفقیت حذف شد.")
    return redirect('drink-detail', drink_id)





