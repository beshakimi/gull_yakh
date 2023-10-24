
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel

# dashboar_view
def dashboar_view(request):
    return render(request, 'admin/dashboard.html')


# add food view 
def create_food_model_view(request):
    foods = foodModel.objects.all().order_by('-id')
    if request.method == 'POST':
 
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        Image = request.FILES['image']
        food = foodModel(Title=Title, Price=Price, Description=Description, Image=Image)
        food.save()
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
    drink = DringModel.objects.all().order_by('-id')
    if request.method == 'POST':
 
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        Image = request.FILES['image']
        drink = DringModel(Title=Title, Price=Price, Description=Description, Image=Image)
        drink.save()
        return redirect('/manage/addDrink')
 
    context = {
        'drinks':drink
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
        image = request.FILS['image']

        post=BlogModel(Title=title, Description=description, Date=date, Image=image)
        post.save
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

        
        


    
    
