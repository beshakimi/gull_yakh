
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from addProducts.models import foodModel
# Create your views here.
def index(request):
    return render(request, 'admin/dashboard.html')



def create_food_model_view(request):
    foods = foodModel.objects.all().order_by('-id')
    if request.method == 'POST':
 
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        Image = request.FILES['image']
        food = foodModel(Title=Title, Price=Price, Description=Description, Image=Image)
        food.save()
        return redirect('/manage/dashboard')
 
    context = {
        'foods':foods
    }
    return render(request, 'admin/addFood.html', context)


def update_food_model_view(request, food_id):
    food = get_object_or_404(foodModel, id=food_id)
    
    if request.method == 'POST':
        Title = request.POST['title']
        Price = request.POST['price']
        Description = request.POST['description']
        Image = request.FILES['image']
        
        food.Title = Title
        food.Price = Price
        food.Description = Description
        food.Image = Image
        food.save()
        
        return redirect('/manage/dashboard')
    else:
        return render(request, 'admin/updatefood.html', {'food': food})
    


def delete_food(request, food_id):
    food = foodModel.objects.get(id=food_id)
    
    if request.method == 'POST':
        food.delete()
        return redirect('create-food')
    
    return render(request, 'admin/delete_food.html', {'food': food})
