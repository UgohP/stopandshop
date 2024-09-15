from django.db import models
from tokenize import blank_re
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from users.models import *

# Create your models here.
class Food(models.Model):
    negotiate = [
        ('Negotiable', 'Negotiable'),
        ('Unnegotiable', 'Unnegotiable'),
    ]
    food_vendor = models.ForeignKey(Vendor, related_name='food_vendors', on_delete=models.CASCADE, null=True)
    food_name = models.CharField(max_length=50)
    food_price = models.FloatField()
    haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
    slug = models.SlugField(null=True, blank=True)
    food_discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', null=True)
    image2 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image3 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image4 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image5 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.food_name)
        super(Food,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.food_name

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

    class Meta:
        ordering = ('-created',)
