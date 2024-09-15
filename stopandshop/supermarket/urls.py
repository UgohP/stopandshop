from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('supermarket/', supermarket, name='supermarket'),
    path('get_supermarket/<int:pk>/', getSupermarket, name='get_supermarket'),
    path('create_supermarket/',createSupermarket, name='create_supermarket'),
    path('supermarket_history/', supermarketHistory, name='supermarket_history'),
    path('update_supermarket/<int:pk>/', updateSupermarket, name='update_supermarket'),
    path('delete_supermarket/<int:pk>/', deleteSupermarket, name='delete_supermarket'),
]