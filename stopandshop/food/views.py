from django.shortcuts import render
from email.mime import application
from itertools import product
import random
from ssl import create_default_context
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from bluemartin.filters import *
from django.contrib.auth.decorators import login_required
from bluemartin.decorators import *
from django.views.generic import ListView
from django.views.generic.edit import *

# Create your views here.
@login_required(login_url='login')
def food(request):
    foods = Food.objects.all()
    context = {'foods':foods}
    return render(request, 'food.html', context)


@login_required(login_url='login')
def getFood(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food':food}
    return render(request, 'get_food.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createFood(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            food = form.save(commit=False)
            food.food_vendor = request.user.vendor

            food.save()   
            messages.success(request, str(food.food_name) + ' was created Successfully!!')
            return redirect('food_history')
    else:
        form = FoodForm()
    context = {'form':form}
    return render(request, 'create_food.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateFood(request, pk):
    food = Food.objects.get(id=pk)
    form = FoodForm(instance=food)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('food_history')
    context = {'form':form}
    return render(request, 'update_food.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteFood(request, pk):

    food = Food.objects.get(id=pk)
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('food_history')
    context = {'food': food}
    return render(request, 'delete_food.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def foodHistory(request):
    vendor = request.user.vendor
    food = Food.objects.filter(food_vendor=vendor)

    context = {'food':food}
    return render(request, 'food_history.html', context)
