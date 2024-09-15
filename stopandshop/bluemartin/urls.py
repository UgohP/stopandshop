from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', blue, name = 'bluemartin'),
    path('hompage/', home, name = 'home'),
    path('categories/', categories, name='categories'),
    path('terms_and_conditions/', TermsAndConditions, name='terms'),
]