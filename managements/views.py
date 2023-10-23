
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from addProducts.models import foodModel
from addProducts.models import DringModel

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
        
        return redirect('/manage/dashboard')
    else:
        return render(request, 'admin/updatefood.html', {'food': food})
    

# delete food view 
def delete_food(request, food_id):
    food = foodModel.objects.get(id=food_id)
    
    if request.method == 'POST':
        food.delete()
        return redirect('create-food')
   

    # add drink view 
def create_drink_model_view(request):
    drinks = DringModel.objects.all().order_by('-id')
    if request.method == 'POST':
 
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        Image = request.FILES['image']
        food = DringModel(Title=Title, Price=Price, Description=Description, Image=Image)
        food.save()
        return redirect('/manage/addDrink')
 
    context = {
        'drink':drinks
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
        
        return redirect('/manage/dashboard')
    else:
        return render(request, 'admin/updatedrink.html', {'drink': drink})
    

# delete drink view 
def delete_drink(request, drink_id):
    drink = DringModel.objects.get(id=drink_id)
    
    if request.method == 'POST':
        drink.delete()
        return redirect('create-drink')
    
    
