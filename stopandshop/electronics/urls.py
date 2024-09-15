from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('electronic/', electronic, name='electronic'),
    path('get_electronic/<int:pk>/', getElectronic, name='get_electronic'),
    path('create_electronic/',createElectronic, name='create_electronic'),
    path('electronic_history/', electronicHistory, name='electronic_history'),
    path('update_electronic/<int:pk>/', updateElectronic, name='update_electronic'),
    path('delete_electronic/<int:pk>/', deleteElectronic, name='delete_electronic'),
]