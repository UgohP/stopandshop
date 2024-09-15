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
def service(request):
    service = Service.objects.all()

    context = {'service':service}

    return render(request, 'service.html', context)
@login_required(login_url='login')

def getService(request, pk):
    service = Service.objects.get(id=pk)
    context = {'service':service}
    return render(request, 'get_service.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)

        if form.is_valid():
            service = form.save(commit=False)
            service.service_vendor = request.user.vendor

            service.save()   
            messages.success(request, 'Service for '+str(service.profession) + ' was created Successfully!!')
            return redirect('service_history')
    else:
        form = ServiceForm()
    context = {'form':form}
    return render(request, 'create_service.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateService(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('service_history')
    context = {'form':form}
    return render(request, 'update_service.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteService(request, pk):

    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('service_history')
    context = {'service': service}
    return render(request, 'delete_service.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def serviceHistory(request):
    vendor = request.user.vendor
    service = Service.objects.filter(service_vendor=vendor)

    context = {'service':service}
    return render(request, 'service_history.html', context)
