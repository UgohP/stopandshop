# from email.mime import application
# from itertools import product
# import random
# from ssl import create_default_context
# from django.shortcuts import render, redirect
# from .models import *
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from .forms import *
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from .filters import *
# from django.contrib.auth.decorators import login_required
# from .decorators import *
# from django.views.generic import ListView
# from django.views.generic.edit import *


# # Create your views here.
# def signupPage(request):
#     form = SignupForm()

#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('login')

#     context = {'form': form}
#     return render (request, 'sign_up.html', context)


# def loginPage(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('vendor_profile')
#         else:
#             messages.info(request, 'Username or password is incorrect') 

#     context = {}
#     return render (request, 'login.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('home')

# @login_required(login_url='login')
# # @allowed_users(allowed_roles=['vendor'])
# def customerProfile(request):
#     customer = request.user.customer
#     form = CustomerForm(instance=customer)
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.info(request, 'Please fill the form')
#     context = {'form': form}

#     return render(request, 'customer/customer_profile.html', context)

# @login_required(login_url='login')
# def customerBase(request):
#     return render(request, 'customer/customer.html')


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def vendorProfile(request):
#     vendor = request.user.vendor
#     form = VendorForm(instance=vendor)
#     if request.method == 'POST':
#         form = VendorForm(request.POST, request.FILES, instance=vendor)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.info(request, 'Please fill the form')
#     context = {'form': form}
#     return render (request, 'vendor/vendor_profile.html', context)

# def vendorDetail(request, pk):
#     user  = User.objects.get(id=pk)


#     context = {'user': user,}
#     return render(request, 'vendor/vendor_detail.html', context)


# @login_required(login_url='login')
# def vendorApplication(request):
#     if request.method == 'POST':
#         form = VendorApplicationForm(request.POST)

#         if form.is_valid():
#             application = form.save(commit=False)
#             application.user = request.user

#             application.save()
#             messages.success(request, 'Application Submitted Successfully')
#             return redirect('customer_profile')
        
#     else:
#         form = VendorApplicationForm()

#     context = {'form':form}
#     return render(request, 'vendor/vendor_application.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def createProduct(request):
#     # categories = Fashion.objects.all()
#     # vendor = Vendor.objects.all()
#     # size = Size.objects.all()
#     # product = Product.objects.all()
#     # vendor = request.user.vendor
#     # form = ProductForm(initial={'created_by':vendor})
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)

#         if form.is_valid():
#             product = form.save(commit=False)
#             product.created_by = request.user.vendor

#             product.save()
#         # data = request.POST
#         # product_images = request.FILES.getlist('product_images')

#         # if data['category'] != 'none':
#         #     category = Fashion.objects.get(id=data['category'])
#         # else:
#         #     category == None

#         # for product_images in product_images:
#         #     photo = Product.objects.create(
#         #         created_by = vendor,
#         #         product_name = data['product_name'],
#         #         product_image = product_images,
#         #         gender = data['gender'],
#         #         category = category,
#         #         price = data['price'],
#         #         haggle = data['haggle'],
#         #         # sizes = data['sizes']
#         #         description = data['description'],
#         #     )  
#         #     photo.save()              
#             messages.success(request, str(product.product_name) + ' was created Successfully!!')
#             return redirect('history')
#     else:
#         form = ProductForm()
        
#     #     form = ProductForm(request.POST, request.FILES, initial={'created_by': vendor})
#     #     product_image = request.FILES.get('product_images')

#     #     image = Product.objects.create(
#     #         product_image=product_image
#     #     )

#     #     if form.is_valid() and image:
#     #         form.save()
#     #         messages.success(request, 'Created Successfully!!')
#     context = {'form':form}
#     return render(request, 'create_product.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def myBlog(request):
#     vendor = request.user.vendor
#     blog = Blog.objects.filter(posted_by=vendor) 

#     context = {'blog':blog}
#     return render(request, 'vendor/my_blog.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def updateProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     form = ProductForm(instance=product)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Updated Successfully!!')
#             return redirect('history')
#     context = {'form':form}
#     return render(request, 'update_product.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def deleteProduct(request, pk):

#     product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         product.delete()
#         messages.success(request, 'Dealeted Successfully!!')
#         return redirect('history')
#     context = {'product': product}
#     return render(request, 'delete_product.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def vendor(request):
#     context = {}
#     return render(request, 'vendor/vendor.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
# def history(request):
#     vendor = request.user.vendor
#     product = Product.objects.filter(created_by=vendor)

#     context = {'product':product}
#     return render(request, 'vendor/history.html', context)

# def home(request):
#     vendor = Vendor.objects.all()
#     carousel = Carousel.objects.all()
#     category = Categorie.objects.all()
#     product = Product.objects.all()[0:5]
#     blog = Blog.objects.all()[0:6]
#     product_image = ProductImage.objects.all()
#     blogfile = BlogFile.objects.all()
#     food = Food.objects.all()
#     foodimage = FoodImage.objects.all()
#     # product = list(Product.objects.all())
#     # product = random.sample(product, 6)
#     context = {'vendor': vendor, 'carousel':carousel, 'category':category, 'product':product, 'blog':blog, 'product_image':product_image, 'food':food, 'foodimage':foodimage, 'blogfile':blogfile}
#     return render(request, 'homepage.html', context) 

# # def sub_category(request, sub_cat):
# #     categorie = Categorie.objects.get(category_name=sub_cat)
# #     sub = SubCategorie.objects.filter(category=categorie)

# #     return render(request, 'sub_category.html', {'sub':sub})

# @login_required(login_url='login')

# def categories(request):
    
#     context = {}
#     return render(request, 'categories/categories.html', context)

# @login_required(login_url='login')
# def blogs(request):
#     blog = Blog.objects.all()
#     vendor = Vendor.objects.all()
#     blogfile = BlogFile.objects.all()
#     context = {'blog':blog, 'blogfile':blogfile,'vendor': vendor,}
#     return render(request, 'blog.html', context)

# @login_required(login_url='login')

# def getBlog(request, pk):
#     blog = Blog.objects.get(id=pk)
#     context = {'blog':blog}
#     return render(request, 'get_blog.html', context)


# @login_required(login_url='login')

# def fashionCategory(request):
    
#     fashion = Fashion.objects.all()
#     context = {'fashion':fashion}
#     return render(request, 'categories/fashion_category.html', context)

# @login_required(login_url='login')

# def food(request):
#     foods = Food.objects.all()

#     context = {'foods':foods}

#     return render(request, 'categories/food.html', context)
# @login_required(login_url='login')

# def getFood(request, pk):
#     food = Food.objects.get(id=pk)
#     context = {'food':food}
#     return render(request, 'get_category/get_food.html', context)

# @login_required(login_url='login')

# def supermarket(request):
#     supermarket = SuperMarket.objects.all()

#     context = {'supermarket':supermarket}

#     return render(request, 'categories/supermarket.html', context)


# @login_required(login_url='login')

# def getSupermarket(request, pk):
#     supermarket = SuperMarket.objects.get(id=pk)
#     context = {'supermarket':supermarket}
#     return render(request, 'get_category/get_supermarket.html', context)
# @login_required(login_url='login')

# def crypto(request):
#     btc = Crypto.objects.all()

#     context = {'btc':btc}

#     return render(request, 'categories/crypto.html', context)
# @login_required(login_url='login')

# def getCrypto(request, pk):
#     btc = Crypto.objects.get(id=pk)
#     context = {'btc':btc}
#     return render(request, 'get_category/get_crypto.html', context)
# @login_required(login_url='login')

# def electronic(request):
#     electronic = Electronic.objects.all()

#     context = {'electronic':electronic}

#     return render(request, 'categories/electronic.html', context)
# @login_required(login_url='login')

# def getElectronic(request, pk):
#     electronic = Electronic.objects.get(id=pk)
#     context = {'electronic':electronic}
#     return render(request, 'get_category/get_electronic.html', context)
# @login_required(login_url='login')

# def service(request):
#     services = Service.objects.all()

#     context = {'services':services}

#     return render(request, 'categories/service.html', context)
# @login_required(login_url='login')

# def getService(request, pk):
#     services = Service.objects.get(id=pk)
#     context = {'services':services}
#     return render(request, 'get_category/get_service.html', context)
# @login_required(login_url='login')

# def fashionProduct(request, fash_pro):
#     vendor = Vendor.objects.all()
#     fashion = Fashion.objects.get(fashion_category=fash_pro)
#     product = Product.objects.filter(category=fashion)
#     myfilter = ProductFilter(request.GET, queryset=product)
#     product = myfilter.qs
#     context = {'vendor': vendor, 'product':product, 'myfilter':myfilter}
    
#     return render(request, 'categories/fashion.html', context)
# @login_required(login_url='login')

# def getFashion(request, pk):
#     fashion = Product.objects.get(id=pk)

#     context = {'fashion':fashion}

#     return render(request, 'get_category/get_fashion.html', context) 




# # class BlogInline():
# #     form_class = BlogForm
# #     model = Blog
# #     template_name = 'create_blog.html'

# #     def form_valid(self, form):
# #         named_formsets = self.get_named_formsets()
# #         if not all((x.is_valid() for x in named_formsets.values())):
# #             return self.render_to_response(self.get_context_data(form=form))

# #         self.object = form.save()

# #         for name, formset in named_formset.items():
# #             formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
# #             if formset_save_func is not None:
# #                 formset_save_func(formset)
# #             else:
# #                 formset.save()
# #         return redirect('blogs:list_blogs')

# #     def formset_images_valid(self, formset):
# #         blogfiles = formset.save(commit=False)
# #         for obj in formset.deleted_objects:
# #             obj.delete(
# #             )
# #         for blogfile in blogfiles:
# #             blogfile.blog = self.object
# #             image.save()

# # class BlogCreate(BlogInline, CreateView):
# #     def get_context_data(self, **kwargs):
# #         ctx = super(BlogCreate, self).get_context_data(**kwargs)
# #         ctx['named_formsets'] = self.get_named_formsets()
# #         return ctx

# #     def get_named_formsets(self):
# #         if self.request.method == "GET":
# #             return {
# #                 'blogfiles': BlogFileFormSet(prefix='blogfiles'),
# #             }
# #         else:
# #             return {
# #                 'blogfiles':BlogFileFormSet(self.request.POST or None, self.request.FILES or None, prefix='blogfiles'),
# #             }

# # class BlogUpdate(BlogInline, UpdateView):
# #     def get_context_data(self, **kwargs):
# #         ctx = super(BlogUpdate, self).get_context_data(**kwargs)
# #         ctx['named_formsets'] = self.get_named_formsets()
# #         return ctx
    
# #     def get_named_formsets(self):
# #         return{
# #             'blogfiles': BlogFileFormSet(self.req)
# #         }

# # class BlogList(ListView):
# #     model = Blog
# #     template_name = 'blog_list.html'
# #     context_object_name= 'blogs'


# class BlogCreateView(CreateView):
#     form_class = BlogForm
#     template_name = 'create_blog.html'

#     def get_context_data(self, **kwargs):
#         context = super(BlogCreateView, self).get_context_data(**kwargs)
#         context['blog_file_formset'] = BlogFileFormSet() 
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         blog_file_formset = BlogFileFormSet(self.request.POST, self.request.FILES)
#         if form.is_valid() and blog_file_formset.is_valid():
#             return self.form_valid(form, blog_file_formset)
#         else:
#             return self.form_invalid(form, blog_file_formset)

#     def form_valid(self, form, blog_file_formset):
#         self.object = form.save(commit=False)
#         self.object.save()
        
#         blog_file = blog_file_formset.save(commit= False)
#         for file in blog_file:
#             file.blog = self.object
#             file.save()
#             return redirect('my_blog')

#     def form_invalid(self, form, blog_file_formset):
#         return self.render_to_response(self.get_context_data(form=form, blog_file_formset=blog_file_formset))