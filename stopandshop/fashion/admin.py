from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'product_name', 'category', 'created']
    model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Fashion)
