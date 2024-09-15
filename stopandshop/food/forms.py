# from pyexpat import model
from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# from product.models import Customer
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['slug', 'food_vendor']