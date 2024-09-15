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
def electronic(request):
    electronic = Electronic.objects.all()
    context = {'electronic':electronic}
    return render(request, 'electronic.html', context)


@login_required(login_url='login')
def getElectronic(request, pk):
    electronic = Electronic.objects.get(id=pk)
    context = {'electronic':electronic}
    return render(request, 'get_electronic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createElectronic(request):
    if request.method == 'POST':
        form = ElectronicForm(request.POST, request.FILES)

        if form.is_valid():
            electronic = form.save(commit=False)
            electronic.electronics_vendor = request.user.vendor

            electronic.save()   
            messages.success(request, str(electronic.electronics_name) + ' was created Successfully!!')
            return redirect('electronic_history')
    else:
        form = ElectronicForm()
    context = {'form':form}
    return render(request, 'create_electronic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateElectronic(request, pk):
    electronic = Electronic.objects.get(id=pk)
    form = ElectronicForm(instance=electronic)
    if request.method == 'POST':
        form = ElectronicForm(request.POST, request.FILES, instance=electronic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('electronic_history')
    context = {'form':form}
    return render(request, 'update_electronic.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteElectronic(request, pk):

    electronic = Electronic.objects.get(id=pk)
    if request.method == 'POST':
        electronic.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('electronic_hostory')
    context = {'electronic': electronic}
    return render(request, 'delete_electronic.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def electronicHistory(request):
    vendor = request.user.vendor
    electronic = Electronic.objects.filter(electronics_vendor=vendor)

    context = {'electronic':electronic}
    return render(request, 'electronic_history.html', context)

