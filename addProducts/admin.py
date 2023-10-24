from django.contrib import admin
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel


# Register your models here.
admin.site.register(foodModel)
admin.site.register(DringModel)
admin.site.register(BlogModel)

