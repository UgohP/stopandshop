import random
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from .filters import *
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.views.generic import ListView
from django.views.generic.edit import *
from users.models import *
from fashion.models import *
from blogs.models import *
from supermarket.models import *
from services.models import *
from food.models import *
from electronics.models import *

# Create your views here.
@login_required(login_url='login')
def home(request):
    vendor = Vendor.objects.all()
    carousel = Carousel.objects.all()
    category = Categorie.objects.all()
    product = Product.objects.all()[0:5]
    blog = Blog.objects.all()[0:6]
    food = Food.objects.all()
    context = {'vendor': vendor, 'carousel':carousel, 'category':category, 'product':product, 'blog':blog, 'food':food,}
    return render(request, 'homepage.html', context)

@login_required(login_url='login')
def categories(request):
    context = {}
    return render(request, 'categories.html', context)

@login_required(login_url='login')
def blue(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user

            application.save()
            messages.success(request, 'SENT')
            return redirect('bluemartin')
        
    else:
        form = ContactUsForm()
    context = {'form':form}
    
    return render(request, 'bluemartin.html', context)

def TermsAndConditions(request):
    context = {}
    return render(request, 'terms_and_conditions.html', context)