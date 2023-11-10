
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.contrib.auth import get_user_model


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("User must have email") 
        if not username:
            raise ValueError("User must have username")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self , email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.user_type = 'ادمین'
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    USER_CHOICES = (
        ('ادمین', 'ادمین'),
        ('کاربر عادی', 'کاربر عادی'),
    )
    email = models.EmailField(max_length=300, unique=True)
    username = models.CharField(max_length=255)
    
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices= USER_CHOICES , default='کاربر عادی')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)




    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email
    

    def get_email(self):
        return self.email

class Profile(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'مرد'),
        ('FEMALE', 'زن'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="user/", null=True, blank=True, default='user/defult_image.png')
    phone = models.CharField(max_length=50, null=True, blank=True, default='')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='MALE')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
   
