from pyexpat import model
from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['posted_by', 'slug']

class BlogVideoForm(forms.ModelForm):
    class Meta:
        model = BlogVideo
        exclude = ['posted_by', 'slug']