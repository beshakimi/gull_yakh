from django.contrib import admin
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel
from addProducts.models import ProfileModel

# Register your models here.
admin.site.register(foodModel)
admin.site.register(DringModel)
admin.site.register(BlogModel)
admin.site.register(ProfileModel)