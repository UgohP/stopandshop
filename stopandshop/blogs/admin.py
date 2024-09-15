from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['posted_by', 'business_name']
    model = Blog
admin.site.register(Blog, BlogAdmin)