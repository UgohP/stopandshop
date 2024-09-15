# Create your models here.
from tokenize import blank_re
from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User 
from bluemartin.models import *

class VendorApplication(models.Model):
    states = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Kastina', 'Kastina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
        ('FCT (Abuja)', 'FCT (Abuja)'),
    ]

    about_us = [
        ('WhatsApp', 'WhatsApp'),
        ('Instagram', 'Instagram'),
        ('X or Twitter', 'X or Twitter'),
        ('Someone', 'Someone'),
        ('Other', 'Other'),
    ]

    categories = [
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Supermarket', 'Supermarket'),
        ('Electronics', 'Electronics'),
        ('Services', 'Services')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_type = models.CharField(max_length=100, choices=categories, null=True)
    business_name = models.CharField(max_length=50)
    state = models.CharField(max_length=100, choices=states, null=True)
    location = models.TextField(null=True)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    business_WhatsApp_number = models.IntegerField()
    how_did_you_here_about_us = models.CharField(max_length=100, choices=about_us, null=True)


    def __str__(self) -> str:
        return str(self.user)
    


class Vendor(models.Model):
    states = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Kastina', 'Kastina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
        ('FCT (Abuja)', 'FCT (Abuja)'),
    ]
        
    business_name = models.CharField(max_length=500, null=True)
    vendor = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    state = models.CharField(max_length=100, choices=states, null=True)
    location = models.TextField(null=True)
    vendor_email = models.EmailField(blank=True)
    business_logo_if_any = models.ImageField(upload_to='image/', null=True, blank=True)
    vendor_phone_number1 = models.IntegerField(null=True)
    vendor_phone_number2 = models.IntegerField(null=True, blank=True)
    business_whatsapp_number = models.CharField(max_length=500, null=True )
    instagram_username = models.CharField(max_length=500, blank=True)
    X_or_twitter_username = models.CharField(max_length=500, blank=True, null=True)
    fashion_vendor = models.BooleanField(default=False, blank=True)
    food_vendor = models.BooleanField(default=False, blank=True)
    supermarket_vendor = models.BooleanField(default=False, blank=True)
    electronics_vendor = models.BooleanField(default=False, blank=True)
    services_vendor = models.BooleanField(default=False, blank=True)
    blog_vendor = models.BooleanField(default=False, blank=True)
    is_premium = models.BooleanField(default=False, blank=True)
    premium_1 = models.BooleanField(default=False, blank=True)
    premium_2 = models.BooleanField(default=False, blank=True)
    premium_3 = models.BooleanField(default=False, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.business_name)
        super(Vendor,self).save(*args, **kwargs)



    def __str__(self):
        return str(self.vendor)

    @property
    def imageURL(self):
        try:
            url = self.business_logo_if_any.url
        except:
            url = ''
        return url
    
class Premium1Application(models.Model):
    categories = [
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Supermarket', 'Supermarket'),
        ('Electronics', 'Electronics'),
        ('Services', 'Services')
    ]
    user = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    business_type1 = models.CharField(max_length=100, choices=categories, null=True)
    business_type2 = models.CharField(max_length=100, choices=categories, null=True)
    business_name = models.CharField(max_length=50)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    business_WhatsApp_number = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)
    
class Premium2Application(models.Model):
    categories = [
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Supermarket', 'Supermarket'),
        ('Electronics', 'Electronics'),
        ('Services', 'Services')
    ]
    user = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    business_type1 = models.CharField(max_length=100, choices=categories, null=True)
    business_type2 = models.CharField(max_length=100, choices=categories, null=True)
    business_type3 = models.CharField(max_length=100, choices=categories, null=True)
    business_name = models.CharField(max_length=50)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    business_WhatsApp_number = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)
    
class Premium3Application(models.Model):
    categories = [
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Supermarket', 'Supermarket'),
        ('Electronics', 'Electronics'),
        ('Services', 'Services')
    ]
    user = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    business_type1 = models.CharField(max_length=100, choices=categories, null=True)
    business_type2 = models.CharField(max_length=100, choices=categories, null=True)
    business_type3 = models.CharField(max_length=100, choices=categories, null=True)
    business_type4 = models.CharField(max_length=100, choices=categories, null=True)
    business_type5 = models.CharField(max_length=100, choices=categories, null=True)
    business_name = models.CharField(max_length=50)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    business_WhatsApp_number = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)

class VendorVerification(models.Model):
    means_of_identification = [
        ("NIN", "NIN"),
        ("Driver's Lincense", "Driver's Lincense"),
        ("Student_ID", "Student_ID"),
        ("Voter's Card", "Voter's Card"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True)
    Means_of_Identification = models.CharField(max_length=100, choices=means_of_identification, null=True)
    front_view = models.ImageField(upload_to='images/', null=True)
    back_view = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
    
    
class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11, null=True)
    is_vendor = models.BooleanField(default=False, null=True, blank=True)
    is_premium = models.BooleanField(default=False, null=True, blank=True)
    in_process = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.customer).capitalize()
    
class CustomerPremiumAppplication(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone_number1 = models.CharField(max_length=11, null=True)
    phone_number2 = models.CharField(max_length=11, null=True)
    
    def __str__(self) -> str:
        return str(self.customer).capitalize()


class SecurityQuestion(models.Model):
    username = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True)
    question1 = models.CharField(max_length=255, default="What is your username", blank=True)
    answer1 = models.CharField(max_length=255, default="", blank=True)
    question2 = models.CharField(max_length=255, default="What is your favourite colour?", blank=True)
    answer2 = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)