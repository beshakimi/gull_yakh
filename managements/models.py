from django.db import models

# Create your models here.
class GetOrder(models.Model):
    customer_name = models.CharField(max_length=200)
    phone_number1 = models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
   
