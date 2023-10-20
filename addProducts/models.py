from django.db import models
from django import forms
from hijri_converter import Hijri

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


    def __str__(self):
        return self.Title


class BlogModel(models.Model):
    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست ها"
    Title=models.CharField(max_length=100 ,verbose_name="عنوان پست")
    Image=models.ImageField(upload_to="blogeImage/", verbose_name="عکس")
    Date=models.DateField(verbose_name="تاریخ")
    Description=models.CharField(max_length=500 ,verbose_name="توضیحات")

    def __str__(self):
        return self.Title
    



class ProfileModel(models.Model):
    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربر ها"
    Name= models.CharField(max_length=100 ,verbose_name="نام ")
    Family= models.CharField(max_length=100 ,verbose_name="نام فامیلی")
    ProfileImage=models.ImageField(upload_to="profileImage/" ,verbose_name="عکس")

    man=1
    woman=2
    status_chioces=(("man","مرد"),("woman","زن"))

    Gender=models.IntegerField(choices=status_chioces,verbose_name="جنسیت")

    def __str__(self):
        return "FullName:{} {}".format("Name,Family")
    


