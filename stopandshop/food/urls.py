from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('food/', food, name='food'),
    path('get_food/<int:pk>/', getFood, name='get_food'),
    path('create_food/',createFood, name='create_food'),
    path('food_history/', foodHistory, name='food_history'),
    path('update_food/<int:pk>/', updateFood, name='update_food'),
    path('delete_food/<int:pk>/', deleteFood, name='delete_food'),
]