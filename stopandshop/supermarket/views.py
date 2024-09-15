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
def supermarket(request):
    supermarket = SuperMarket.objects.all()
    context = {'supermarket':supermarket}
    return render(request, 'supermarket.html', context)


@login_required(login_url='login')
def getSupermarket(request, pk):
    supermarket = SuperMarket.objects.get(id=pk)
    context = {'supermarket':supermarket}
    return render(request, 'get_supermarket.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createSupermarket(request):
    if request.method == 'POST':
        form = SupermarketForm(request.POST, request.FILES)
        if form.is_valid():
            supermarket = form.save(commit=False)
            supermarket.market_vendor = request.user.vendor

            supermarket.save()   
            messages.success(request, str(supermarket.item_name) + ' was created Successfully!!')
            return redirect('supermarket_history')
    else:
        form = SupermarketForm()
    context = {'form':form}
    return render(request, 'create_supermarket.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateSupermarket(request, pk):
    supermarket = SuperMarket.objects.get(id=pk)
    form = SupermarketForm(instance=supermarket)
    if request.method == 'POST':
        form = SupermarketForm(request.POST, request.FILES, instance=supermarket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('supermarket_history')
    context = {'form':form}
    return render(request, 'update_supermarket.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteSupermarket(request, pk):
    supermarket = SuperMarket.objects.get(id=pk)
    if request.method == 'POST':
        supermarket.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('supermarket_history')
    context = {'supermarket': supermarket}
    return render(request, 'delete_supermarket.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def supermarketHistory(request):
    vendor = request.user.vendor
    supermarket = SuperMarket.objects.filter(market_vendor=vendor)

    context = {'supermarket':supermarket}
    return render(request, 'supermarket_history.html', context)
