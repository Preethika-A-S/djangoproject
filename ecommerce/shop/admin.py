from django.contrib import admin

# Register your models here.
from shop.models import Category
admin.site.register(Category)

from shop.models import Product
admin.site.register(Product)