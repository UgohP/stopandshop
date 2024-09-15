from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('crypto/', crypto, name='crypto'),
    path('get_crypto/<int:pk>/', getCrypto, name='get_crypto'),
]