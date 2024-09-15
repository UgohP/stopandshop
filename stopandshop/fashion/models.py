from django.db import models
from bluemartin.models import *
from django.utils.text import slugify
from django.contrib.auth.models import User
from users.models import *

# Create your models here.
class Fashion(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True) 
    fashion_category = models.CharField(max_length=20)
    category_image = models.ImageField(upload_to='image', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fashion_category)
        super(Fashion,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.fashion_category


class Size(models.Model):
    size = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.size

class Product(models.Model):
    negotiate = [
        ('Negotiable', 'Negotiable'),
        ('Unnegotiable', 'Unnegotiable'),
    ]

    sex = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unisex', 'Unisex'),
    ]

    created_by = models.ForeignKey(Vendor, related_name = "fashion_vendors", on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Fashion, on_delete=models.CASCADE, related_name='product', null=True)
    gender = models.CharField(max_length=10, choices=sex, default='Unisex', null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
    slug = models.SlugField(null=True, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', null=True) 
    image2 = models.ImageField(upload_to = 'images/', null=True, blank= True)    
    image3 = models.ImageField(upload_to = 'images/', null=True, blank= True)    
    image4 = models.ImageField(upload_to = 'images/', null=True, blank= True)    
    image5 = models.ImageField(upload_to = 'images/', null=True, blank= True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.created_by.business_name).capitalize()
        # return self.product_name

    class Meta:
        ordering = ('-created',)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

    @property
    def image4URL(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url
    @property
    def image5URL(self):
        try:
            url = self.image5.url
        except:
            url = ''
        return url

