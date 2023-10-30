from django.db import models
from django import forms
from hijri_converter import Hijri
from django.utils import timezone
from accounts.models import User

# Create your models here.

class foodModel(models.Model):
    class Meta:
        verbose_name="غذا"
        verbose_name_plural="غذا ها"

    Title=models.CharField(max_length=100 ,verbose_name="نام غذا")
    Price=models.IntegerField( verbose_name="قیمت")
    Image=models.ImageField(upload_to="foodImage/" ,verbose_name="عکس")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")

    def __str__(self):
        return self.Title
    


class DringModel(models.Model):
    class Meta:
        verbose_name="نوشیدنی"
        verbose_name_plural="نوشیدنی ها"

    Title=models.CharField(max_length=100 ,verbose_name="نام نوشیدنی")
    Price=models.IntegerField(verbose_name="قیمت")
    Image=models.ImageField(upload_to="dringImage/" ,verbose_name="عکس")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")
    Created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.Title


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

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food = models.ManyToManyField(foodModel, null=True, blank=True)
    drink = models.ManyToManyField(DringModel, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.CharField(max_length=200)
    
    

    


