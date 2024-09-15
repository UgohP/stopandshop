# from pyexpat import model
# from django import forms
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import *

# from product.models import Customer


# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         exclude = ['customer', 'is_vendor']


# class VendorForm(forms.ModelForm):
#     class Meta:
#         model = Vendor
#         exclude = ['vendor', 'fashion_vendor', 'food_vendor', 'supermarket_vendor', 'electronics_vendor', 'services_vendor', 'blog_vendor' ]

# class VendorApplicationForm(forms.ModelForm):
#     class Meta:
#         model = VendorApplication
#         exclude = ['user']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         exclude = ['slug', 'created_by']

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = '__all__'

# class BlogFileForm(forms.ModelForm):
#     class Meta:
#         model = BlogFile
#         fields = '__all__'

# BlogFileFormSet = inlineformset_factory(Blog, BlogFile, form=BlogFileForm, extra=3, can_delete=True, can_delete_extra=True)

