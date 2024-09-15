# from tokenize import blank_re
# from django.db import models
# from django.utils.text import slugify
# from django.contrib.auth.models import User 


# # Create your models here.
# class VendorApplication(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     business_type = models.TextField()
#     business_name = models.CharField(max_length=50)
#     phone_number1 = models.IntegerField()
#     phone_number2 = models.IntegerField(blank=True, null=True)
#     email = models.EmailField(blank=True)
#     business_whatapp_number = models.IntegerField()
#     comments = models.TextField()


# class Vendor(models.Model):
#     business_name = models.CharField(max_length=500, null=True)
#     vendor = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
#     vendor_email = models.EmailField(blank=True)
#     vendor_photo = models.ImageField(upload_to='image', null=True)
#     vendor_phone_number1 = models.IntegerField(null=True)
#     vendor_phone_number2 = models.IntegerField(null=True, blank=True)
#     whatsapp_url = models.CharField(max_length=500)
#     instagram_url = models.CharField(max_length=500, blank=True)
#     fashion_vendor = models.BooleanField(default=False, blank=True)
#     food_vendor = models.BooleanField(default=False, blank=True)
#     supermarket_vendor = models.BooleanField(default=False, blank=True)
#     electronics_vendor = models.BooleanField(default=False, blank=True)
#     services_vendor = models.BooleanField(default=False, blank=True)
#     blog_vendor = models.BooleanField(default=False, blank=True)


    
    # def __str__(self):
    #     return str(self.vendor).capitalize()

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.vendor_photo.url
    #     except:
    #         url = ''
    #     return url

# class Blog(models.Model):
#     posted_by = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     business_name = models.CharField(max_length=30, null=True)
#     text = models.TextField()
#     whatsapp_url = models.CharField(max_length=100, null=True) 
#     blog_image = models.ImageField(upload_to = 'image', null=True, blank=True)
#     blog_image2 = models.ImageField(upload_to = 'image', null=True, blank=True)
#     blog_image3 = models.ImageField(upload_to = 'image', null=True, blank=True)
#     blog_image4 = models.ImageField(upload_to = 'image', null=True, blank=True)
#     blog_image5 = models.ImageField(upload_to = 'image', null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True, null=True)    

#     def __str__(self):
#         return str(self.posted_by).capitalize()

#     @property
#     def imageURL(self):
#         try:
#             url = self.blog_image.url
#         except:
#             url = ''
#         return url

#     @property
#     def image2URL(self):
#         try:
#             url = self.blog_image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.blog_image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.blog_image4.url
#         except:
#             url = ''
#         return url

#     @property
#     def image5URL(self):
#         try:
#             url = self.blog_image5.url
#         except:
#             url = ''
#         return url

#     class Meta:
#         ordering = ('-created',)
# class BlogFile(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
#     blog_file = models.ImageField(upload_to = 'image', null=True, blank=True)    

#     def __str__(self) -> str:
#         return str(self.blog).capitalize()

#     @property
#     def imageURL(self):
#         try:
#             url = self.blog_file.url
#         except:
#             url = ''
#         return url

# class Customer(models.Model):
#     customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customer')
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     email = models.EmailField(blank=True)
#     phone_number = models.CharField(max_length=11, null=True)
#     is_vendor = models.BooleanField(default=False, null=True, blank=True)

#     def __str__(self) -> str:
#         return str(self.customer).capitalize()

# class Carousel(models.Model):
#     carousel = models.ImageField(upload_to = 'image', null=True)

#     def __str__(self):
#         slides = "{}".format(self.carousel)
#         return slides

# class Categorie(models.Model):
#     category_name = models.CharField(max_length=50, null=True)
#     category_image = models.ImageField(upload_to='image', null=True)
#     slug = models.SlugField(unique=True, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.category_name)
#         super(Categorie,self).save(*args, **kwargs)

#     def __str__(self) -> str:
#         return self.category_name

# class Fashion(models.Model):
#     category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True) 
#     fashion_category = models.CharField(max_length=20)
#     category_image = models.ImageField(upload_to='image', null=True, blank=True)
#     slug = models.SlugField(unique=True, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.fashion_category)
#         super(Fashion,self).save(*args, **kwargs)

#     def __str__(self) -> str:
#         return self.fashion_category


# class Size(models.Model):
#     size = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.size


# class Product(models.Model):
#     negotiate = [
#         ('Negotiable', 'Negotiable'),
#         ('Unnegotiable', 'Unnegotiable'),
#     ]

#     sex = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Unisex', 'Unisex'),
#     ]

#     created_by = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     product_name = models.CharField(max_length=100, null=True)
#     category = models.ForeignKey(Fashion, on_delete=models.CASCADE, related_name='product', null=True)
#     gender = models.CharField(max_length=10, choices=sex, default='Unisex', null=True)
#     price = models.DecimalField(decimal_places=2, max_digits=15, null=True)
#     haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
#     sizes = models.ManyToManyField(Size, blank=True)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to = 'image', null=True) 
#     image2 = models.ImageField(upload_to = 'image', null=True, blank= True)    
#     image3 = models.ImageField(upload_to = 'image', null=True, blank= True)    
#     image4 = models.ImageField(upload_to = 'image', null=True, blank= True)    
#     image5 = models.ImageField(upload_to = 'image', null=True, blank= True)    
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return str(self.created_by).capitalize()
#         # return self.product_name

#     class Meta:
#         ordering = ('-created',)
    
#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url

#     @property
#     def image2URL(self):
#         try:
#             url = self.image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.image4.url
#         except:
#             url = ''
#         return url
#     @property
#     def image5URL(self):
#         try:
#             url = self.image5.url
#         except:
#             url = ''
#         return url



# class ProductImage(models.Model):
#     product= models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     product_image = models.ImageField(upload_to = 'image', null=True, blank=True )

#     def __str__(self) -> str:
#         return str(self.product).capitalize()

#     @property
#     def imageURL(self):
#         try:
#             url = self.product_image.url
#         except:
#             url = ''
#         return url

# class Food(models.Model):
#     negotiate = [
#         ('Negotiable', 'Negotiable'),
#         ('Unnegotiable', 'Unnegotiable'),
#     ]
#     food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     food_name = models.CharField(max_length=50)
#     food_price = models.FloatField()
#     haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
#     food_discription = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to = 'image', null=True)
#     image2 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image3 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image4 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image5 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return self.food_name

#     class Meta:
#         ordering = ('-created',)

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url


#     @property
#     def image2URL(self):
#         try:
#             url = self.image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.image4.url
#         except:
#             url = ''
#         return url
#     @property
#     def image5URL(self):
#         try:
#             url = self.image5.url
#         except:
#             url = ''
#         return url

#     class Meta:
#         ordering = ('-created',)

# class FoodImage(models.Model):
#     food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
#     food_image = models.ImageField(upload_to = 'image', null=True, blank=True )

#     def __str__(self) -> str:
#         return str(self.food).capitalize()

#     @property
#     def imageURL(self):
#         try:
#             url = self.food_image.url
#         except:
#             url = ''
#         return url


# class SuperMarket(models.Model):
#     negotiate = [
#         ('Negotiable', 'Negotiable'),
#         ('Unnegotiable', 'Unnegotiable'),
#     ]
#     market_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     item_name = models.CharField(max_length=50)
#     item_price = models.FloatField()
#     haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
#     item_description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to = 'image', null=True)
#     image2 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image3 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image4 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image5 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return self.item_name

#     class Meta:
#         ordering = ('-created',)

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
    
#     @property
#     def image2URL(self):
#         try:
#             url = self.image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.image4.url
#         except:
#             url = ''
#         return url
#     @property
#     def image5URL(self):
#         try:
#             url = self.image5.url
#         except:
#             url = ''
#         return url


# # class SuperMarketImage(models.Model):
# #     item = models.ForeignKey(SuperMarket, on_delete=models.CASCADE, null=True)
# #     item_image = models.ImageField(upload_to = 'image', null=True, blank=True )

# #     def __str__(self) -> str:
# #         return str(self.item).capitalize()

# #     @property
# #     def imageURL(self):
# #         try:
# #             url = self.item_image.url
# #         except:
# #             url = ''
# #         return url

# class Electronic(models.Model):
#     negotiate = [
#         ('Negotiable', 'Negotiable'),
#         ('Unnegotiable', 'Unnegotiable'),
#     ]
#     electronics_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     electronics_name = models.CharField(max_length=50)
#     electronics_price = models.FloatField()
#     haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
#     electronics_description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to = 'image', null=True)
#     image2 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image3 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image4 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     image5 = models.ImageField(upload_to = 'image', null=True, blank=True)    
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return self.electronics_name

#     class Meta:
#         ordering = ('-created',)

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url

#     @property
#     def image2URL(self):
#         try:
#             url = self.image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.image4.url
#         except:
#             url = ''
#         return url
#     @property
#     def image5URL(self):
#         try:
#             url = self.image5.url
#         except:
#             url = ''
#         return url

# class ElectronicImage(models.Model):
#     electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, null=True)
#     electronic_image = models.ImageField(upload_to = 'image', null=True, blank=True )

#     def __str__(self) -> str:
#         return str(self.electronic).capitalize()

#     @property
#     def imageURL(self):
#         try:
#             url = self.electronic_image.url
#         except:
#             url = ''
#         return url

# class Service(models.Model):
#     negotiate = [
#         ('Negotiable', 'Negotiable'),
#         ('Unnegotiable', 'Unnegotiable'),
#     ]
#     service_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     profession = models.CharField(max_length=50)
#     haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
#     location = models.TextField()
#     phone_number_1 = models.PositiveIntegerField(null=True)
#     phone_number_2 = models.PositiveIntegerField(null=True, blank=True)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to = 'image', null=True)
#     image2 = models.ImageField(upload_to = 'image', null=True, blank=True )
#     image3 = models.ImageField(upload_to = 'image', null=True, blank=True )
#     image4 = models.ImageField(upload_to = 'image', null=True, blank=True )
#     image5 = models.ImageField(upload_to = 'image', null=True, blank=True )
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return self.profession

#     class Meta:
#         ordering = ('-created',)

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
    
#     @property
#     def image2URL(self):
#         try:
#             url = self.image2.url
#         except:
#             url = ''
#         return url

#     @property
#     def image3URL(self):
#         try:
#             url = self.image3.url
#         except:
#             url = ''
#         return url

#     @property
#     def image4URL(self):
#         try:
#             url = self.image4.url
#         except:
#             url = ''
#         return url
#     @property
#     def image5URL(self):
#         try:
#             url = self.image5.url
#         except:
#             url = ''
#         return url

# class Crypto(models.Model):
#     crypto_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
#     logo = models.ImageField(upload_to = 'image', null=True, blank=True )
#     discription = models.TextField(blank=True, null=True)

#     @property
#     def imageURL(self):
#         try:
#             url = self.logo.url
#         except:
#             url = ''
#         return url
    
# # class SubCategorie(models.Model):
# #     category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
# #     sub_category_name = models.CharField(max_length=100, null=True)   
# #     sub_category_image = models.ImageField(upload_to='image', blank=True, null=True)
# #     slug = models.SlugField(unique=True, null=True, blank=True)


# #     def save(self, *args, **kwargs):
# #         self.slug = slugify(self.sub_category_name)
# #         super(SubCategorie,self).save(*args, **kwargs)
    
# #     def __str__(self) -> str:
# #         return self.sub_category_name


# # class ProductImage(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     image = models.ImageField(upload_to = 'image')

