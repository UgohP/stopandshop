from audioop import reverse
from django.shortcuts import render

# Create your views here.
from email.mime import application, message
from itertools import product
import random
from ssl import create_default_context
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from bluemartin.filters import *
from django.contrib.auth.decorators import login_required
from bluemartin.decorators import *
from django.views.generic import ListView
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from blogs.models import *
from electronics.models import *
from supermarket.models import *
from fashion.models import *
from food.models import *
from services.models import *
from django.contrib.auth import get_user_model
from django.db.models import Q


def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignupForm()

        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render (request, 'registration/sign_up.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if SecurityQuestion.DoesNotExist:
                    print('not')
                    return redirect('security_questions')
                else:
                    print('done')
                    return redirect('vendor_profile')
            else:
                messages.info(request, 'Username or password is incorrect') 

        context = {}
        return render (request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('logout')
    success_message = 'Your Password has been changed successfully'    
    
        
@login_required(login_url='login')
def set_security_questions(request):
    # try:
    #     security_question = SecurityQuestion.objects.get(user=request.user)
    # except SecurityQuestion.DoesNotExist:
    #     security_question = None

    # if request.method == 'POST':
    #     form = SecurityQuestionForm(request.POST, instance=security_question)
    #     if form.is_valid():
    #         security_question = form.save(commit=False)
    #         security_question.user = request.user
    #         security_question.save()
    #         return redirect('home')
    # else:
    #     form = SecurityQuestionForm(instance=security_question)
    # return render(request, 'set_security_questions.html', {'form':form})

    try:
        security_question = SecurityQuestion.objects.get(username=request.user.customer)
    except SecurityQuestion.DoesNotExist:
        security_question = None
    
    form = SQForm(instance=security_question)
    if request.method == 'POST':
        form = SQForm(request.POST, instance=security_question)
        if form.is_valid():
            security_question = form.save(commit=False)
            security_question.username = request.user.customer
            security_question.save()
            return redirect('customer_profile')

    context = {'form':form}

    return render(request, 'registration/set_security_questions.html', context)


User = get_user_model()
def reset_password(request):
    if request.method == 'POST':
        form = SecurityQuestionForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            answer2 = request.POST.get('answer2')


            user = User.objects.filter(Q(username=username) | Q(email=username)).first()

            if user:
                security_question = user.customer.securityquestion
                if (security_question.answer2 == answer2):
                    request.session['reset_user_id'] = user.id
                    # user = authenticate(request, username=username, password='dummy_password')
                    print(user)
                    login(request, user)
                    return redirect('set_new_password')
                else:
                    print('not')
                    messages.info(request, 'Incorrect Answer') 
            else:
                messages.info(request, "User not found")
    else:
        form = SecurityQuestionForm()
    return render(request, 'registration/reset_password.html', {'form':form})

def set_new_password(request):
    # user_id = request.session.get('reset_user_id')
    # if not user_id:
    #     return redirect('reset_password')

    # user = User.objects.get(pk=user_id)

    # if request.method == 'POST':
    #     form = ResetPasswordForm(request.POST)
    #     if form.is_valid():
    #         new_password = form.cleaned_data['new_password']
    #         confirm_password = form.cleaned_data['confirm_password']

    #         if new_password == confirm_password:
    #             user.set_password(new_password)
    #             user.save
    #             print(user.set_password)

    #             del request.session['reset_user_id']
    #             return redirect('logout')
    #         else:form.add_error(None, 'Passwords do not match')        
    # else:
    #     form = ResetPasswordForm()

    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('logout')
    else:
        form = SetPasswordForm(request.user)

    return render(request, 'registration/set_new_password.html', {'form':form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
# def changePasswordDone(request):
#     messages.success(request, 'Password Changed Successfully!')
#     return render(request, 'customer/customer_profile')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def customerProfile(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.info(request, 'Please fill the form')
    context = {'form': form}

    return render(request, 'customer/customer_profile.html', context)

@login_required(login_url='login')
def customerBase(request):
    return render(request, 'customer/customer.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def vendor(request):
    context = {}
    return render(request, 'vendor/vendor.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def vendorProfile(request):
    vendor = request.user.vendor
    form = VendorForm(instance=vendor)
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.info(request, 'Please fill the form')
    context = {'form': form}
    return render (request, 'vendor/vendor_profile.html', context)


@login_required(login_url='login')
def vendorDetail(request, pk):
    vendor  = Vendor.objects.get(id=pk)
    context = {'vendor': vendor,}
    return render(request, 'vendor/vendor_detail.html', context)


@login_required(login_url='login')
def vendorApplication(request):
    if request.method == 'POST':
        form = VendorApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user

            application.save()
            messages.success(request, 'Application Submitted Successfully. Please Check either your WhatsApp or SMS or Gmail for more information')
            return redirect('customer_profile')
        
    else:
        form = VendorApplicationForm()


    context = {'form':form}
    return render(request, 'vendor/vendor_application.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def premium1Application(request):
    if request.method == 'POST':
        form = Premium1ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user.vendor

            application.save()
            messages.success(request, 'Application Submitted Successfully. Please Check either your WhatsApp or SMS or Gmail for more information')
            return redirect('vendor_profile')
        
    else:
        form = Premium1ApplicationForm()


    context = {'form':form}
    return render(request, 'vendor/premium1_application.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['vendor'])
def premium2Application(request):
    if request.method == 'POST':
        form = Premium2ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user.vendor

            application.save()
            messages.success(request, 'Application Submitted Successfully. Please Check either your WhatsApp or SMS or Gmail for more information')
            return redirect('vendor_profile')
        
    else:
        form = Premium2ApplicationForm()


    context = {'form':form}
    return render(request, 'vendor/premium2_application.html', context)

@login_required(login_url='login')
def premium3Application(request):
    if request.method == 'POST':
        form = Premium3ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user.vendor

            application.save()
            messages.success(request, 'Application Submitted Successfully. Please Check either your WhatsApp or SMS or Gmail for more information')
            return redirect('vendor_profile')
        
    else:
        form = Premium3ApplicationForm()


    context = {'form':form}
    return render(request, 'vendor/premium3_application.html', context)

@login_required(login_url='login')
def premiumCustomerApplication(request):
    if request.method == 'POST':
        form = CustomerPremiumApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user.customer

            application.save()
            messages.success(request, 'Application Submitted Successfully. Please Check either your WhatsApp or SMS or Gmail for more information')
            return redirect('customer_profile')
        
    else:
        form = CustomerPremiumApplicationForm()


    context = {'form':form}
    return render(request, 'customer/customer_premium_application.html', context)


@login_required(login_url='login')
def vendorVerification(request):
    if request.method == 'POST':
        form = VendorVerificationForm(request.POST, request.FILES)

        if form.is_valid():
            verification = form.save(commit=False)
            verification.user = request.user

            verification.save()
            messages.success(request, 'In Process')
            return redirect('customer_profile')
        
    else:
        form = VendorVerificationForm()

    context = {'form':form}
    return render(request, 'vendor/vendor_verification.html', context)