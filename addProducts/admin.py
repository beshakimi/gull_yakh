from django.contrib import admin
from addProducts.models import foodModel
from addProducts.models import DringModel
from addProducts.models import BlogModel, Cart, CartItem, Checkout, FoodComment, DrinkComment, BlogComment, WebsiteComment


# Register your models here.
admin.site.register(foodModel)
admin.site.register(DringModel)
admin.site.register(BlogModel)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Checkout)
admin.site.register(FoodComment)
admin.site.register(DrinkComment)
admin.site.register(BlogComment)
admin.site.register(WebsiteComment)

