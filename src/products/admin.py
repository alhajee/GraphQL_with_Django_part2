from django.contrib import admin
from .models import Product, Category

# Register models in Django Admin
admin.site.register(Product)
admin.site.register(Category)