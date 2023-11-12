from django.db import models
from django import forms
from hijri_converter import Hijri
from django.utils import timezone
from accounts.models import User
from accounts.models import Profile

# Create your models here.

# food model 
class foodModel(models.Model):
    class Meta:
        verbose_name="غذا"
        verbose_name_plural="غذا ها"

    Title=models.CharField(max_length=100 ,verbose_name="نام غذا")
    Price=models.IntegerField( verbose_name="قیمت")
    Image=models.ImageField(upload_to="foodImage/" ,verbose_name="عکس")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")
    Created = models.DateTimeField(default=timezone.now)
    # Category = models.CharField(max_length=100,blank=True, null=True, verbose_name="دسته بندی")

    def __str__(self):
        return self.Title

# drink model 
class DringModel(models.Model):
    class Meta:
        verbose_name="نوشیدنی"
        verbose_name_plural="نوشیدنی ها"

    Title=models.CharField(max_length=100 ,verbose_name="نام نوشیدنی")
    Price=models.IntegerField(verbose_name="قیمت")
    Image=models.ImageField(upload_to="dringImage/" ,verbose_name="عکس")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")
    Created = models.DateTimeField(default=timezone.now)
    # Category = models.CharField(max_length=100, blank=True, null=True, verbose_name="دسته بندی")


    def __str__(self):
        return self.Title

# blog model 
class BlogModel(models.Model):
    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست ها"
    Title=models.CharField(max_length=100 ,verbose_name="عنوان پست")
    Image=models.ImageField(upload_to="blogeImage/", verbose_name="عکس")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.Title

# cart model 
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# chackout model 
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    ordered = models.BooleanField(default=False)
    phone_number1=models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100, null=True, blank=True)
    tazkra_number = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return self.name

# cart itme model 
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(foodModel, on_delete=models.CASCADE, null=True, blank=True)
    drink = models.ForeignKey(DringModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    checkout = models.ForeignKey(Checkout, on_delete=models.SET_NULL, null=True, blank=True)
    checked = models.BooleanField(default=False)
    total_price = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
# drink comment model 
class DrinkComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    drink = models.ForeignKey(DringModel, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment[:30]

# food comment model 
class FoodComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food = models.ForeignKey(foodModel, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment[:30]

# blog comment model 
class BlogComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment[:30]

# WebsiteComment model   
class WebsiteComment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment[:20]

