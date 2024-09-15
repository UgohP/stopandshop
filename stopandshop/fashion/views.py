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
def fashionCategory(request):
    
    fashion = Fashion.objects.all()
    context = {'fashion':fashion}
    return render(request, 'fashion_category.html', context)


@login_required(login_url='login')
def fashionProduct(request, fash_pro):
    vendor = Vendor.objects.all()
    fashion = Fashion.objects.get(fashion_category=fash_pro)
    product = Product.objects.filter(category=fashion)
    myfilter = ProductFilter(request.GET, queryset=product)
    product = myfilter.qs
    context = {'vendor': vendor, 'product':product, 'myfilter':myfilter}
    
    return render(request, 'fashion.html', context)

@login_required(login_url='login')
def getFashion(request, pk):
    fashion = Product.objects.get(id=pk)

    context = {'fashion':fashion}

    return render(request, 'get_fashion.html', context) 



@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user.vendor

            product.save()   
            messages.success(request, str(product.product_name) + ' was created Successfully!!')
            return redirect('history')
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request, 'create_product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('history')
    context = {'form':form}
    return render(request, 'update_product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def deleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Deleated Successfully!!')
        return redirect('history')
    context = {'product': product}
    return render(request, 'delete_product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def history(request):
    vendor = request.user.vendor
    product = Product.objects.filter(created_by=vendor)

    context = {'product':product}
    return render(request, 'history.html', context)
