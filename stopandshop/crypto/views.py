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

def crypto(request):
    btc = Crypto.objects.all()

    context = {'btc':btc}

    return render(request, 'crypto.html', context)
@login_required(login_url='login')

def getCrypto(request, pk):
    btc = Crypto.objects.get(id=pk)
    context = {'btc':btc}
    return render(request, 'get_crypto.html', context)