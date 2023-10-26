
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel
from accounts.models import Profile,User
from accounts import views

# dashboar_view
def dashboar_view(request):
    return render(request, 'admin/dashboard.html')


# add food view 
def create_food_model_view(request):
    foods = foodModel.objects.all().order_by('-id')
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if foodModel.objects.filter(Title=title).exists():
            messages.error(request, 'این مورد از قبل وجود دارد.')
            return redirect('/manage/addfood')

        food = foodModel(Title=title, Price=price, Description=description, Image=image)
        food.save()

        messages.success(request, ' با موفقیت اضافه شد.')
        return redirect('/manage/addfood')

    context = {
        'foods':foods
    }

    return render(request, 'admin/addFood.html', context)
    

# update food view 
def update_food_model_view(request, food_id):
    food = get_object_or_404(foodModel, id=food_id)
    
    if request.method == 'POST':
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        
        if 'image' in request.FILES:
            Image = request.FILES['image']
            food.Image = Image

        food.Title =Title
        food.Price = Price
        food.Description = Description
        
        food.save()
        
        return redirect('create-food')
    else:
        return render(request, 'admin/updatefood.html', {'food': food})
    

# delete food view 
def delete_food(request, food_id):
    food = foodModel.objects.get(id=food_id)
    
    if request.method == 'POST':
        food.delete()
        return redirect('create-food')
   

    # add drink view 
def create_drink_view(request):
    drinks = DringModel.objects.all().order_by('-id')

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # if not title:
        #     messages.error(request, 'لطفا نام را وارد کنید.')
        #     return redirect('/manage/addDrink')
        # if not price:
        #     messages.error(request, 'لطفا قیمت را وارد کنید.')
        #     return redirect('/manage/addDrink')
        # if not description:
        #     messages.error(request, 'لطفا توضیحات را وارد کنید.')
        #     return redirect('/manage/addDrink')
        # if not image:
        #     messages.error(request, 'لطفا عکس را وارد کنید.')
        #     return redirect('/manage/addDrink')

      
        if DringModel.objects.filter(Title=title).exists():
            messages.error(request, 'این مورد از قبل وجود دارد.')
            return redirect('/manage/addDrink')

        drink = DringModel(Title=title, Price=price, Description=description, Image=image)
        drink.save()

        messages.success(request, ' با موفقیت اضافه شد.')
        return redirect('/manage/addDrink')

    context = {
        'drinks': drinks
    }
    return render(request, 'admin/addDrink.html', context)

# update drink view 
def update_drink_model_view(request, drink_id):
    drink = get_object_or_404(DringModel, id=drink_id)
    
    if request.method == 'POST':
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        
        if 'image' in request.FILES:
            Image = request.FILES['image']
            drink.Image = Image
        
        drink.Title = Title
        drink.Price = Price
        drink.Description = Description
        drink.save()
        
        return redirect('create-drink')
    else:
        return render(request, 'admin/updatedrink.html', {'drink': drink})
    

# delete drink view 
def delete_drink(request, drink_id):
    drink = DringModel.objects.get(id=drink_id)
    
    if request.method == 'POST':
        drink.delete()
        return redirect('create-drink')
    
# add post
def create_post_view(request):
    post=BlogModel.objects.all().order_by('-id')

    if request.method == 'POST':
        title=request.POST['title']
        description= request.POST['description']
        date = request.POST['date']
        image = request.FILES['image']

        post=BlogModel(Title=title, Description=description, Date=date, Image=image)
        post.save()
        return redirect('/manage/addPost')
    context={
        'posts':post
    }
    return render(request, 'admin/addPost.html',context)
    
    # update post view 
def update_post_view(request, post_id):
    post = get_object_or_404(BlogModel, id=post_id)
    
    if request.method == 'POST':
        Title = request.POST['title']
        if 'date' in request.DATES:
            Date = request.POST['date']
            post.Date = Date
        Description = request.POST['description']
        
        if 'image' in request.FILES:
            Image = request.FILES['image']
            post.Image = Image
        
        post.Title = Title
        post.Description = Description
        post.save()
        
        return redirect('/manage/addPost')
    else:
        return render(request, 'admin/updatepost.html', {'post': post})
    

# delete post view 
def delete_post(request, post_id):
    post = BlogModel.objects.get(id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('create-post')
    



# users view 
def user_list_view(request):
    
    users=Profile.objects.all().order_by('-id')
    page = request.GET.get('page')

    # تعداد نوشیدنی‌ها در هر صفحه
    items_per_page = 8

    paginator = Paginator(users, items_per_page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        users = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        users = paginator.page(page)
    
    left_index = (int(page) - 2 )
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    pagination_range = range(left_index, right_index + 1)
    context={
       "userlist":users,
       "pagination_range": pagination_range,
   }
    return render(request,"admin/user.html",context)
        
        


    
    
