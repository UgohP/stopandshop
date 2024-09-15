from django.contrib import admin
from .models import *
# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['food_vendor', 'food_name', 'food_price', 'created']
    model = Food

admin.site.register(Food, FoodAdmin)