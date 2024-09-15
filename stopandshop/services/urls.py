from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('service/', service, name='service'),
    path('get_service/<int:pk>/', getService, name='get_service'),
    path('create_service/', createService, name='create_service'),
    path('update_service/<int:pk>/', updateService, name='update_service'),
    path('delete_service/<int:pk>/', deleteService, name='delete_service'),
    path('history/', serviceHistory, name='service_history'),

    
    ]