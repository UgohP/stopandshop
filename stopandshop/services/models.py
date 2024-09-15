from django.db import models
from tokenize import blank_re
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
from users.models import *

# Create your models here.
class Service(models.Model):
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

    negotiate = [
        ('Negotiable', 'Negotiable'),
        ('Unnegotiable', 'Unnegotiable'),
    ]

    service_vendor = models.ForeignKey(Vendor, related_name='service_vendors', on_delete=models.CASCADE, null=True)
    profession = models.CharField(max_length=50)
    haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
    state = models.CharField(max_length=100, choices=states, null=True)
    location = models.TextField(null=True)
    phone_number_1 = models.PositiveIntegerField(null=True)
    phone_number_2 = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', null=True)
    image2 = models.ImageField(upload_to = 'images/', null=True, blank=True )
    image3 = models.ImageField(upload_to = 'images/', null=True, blank=True )
    image4 = models.ImageField(upload_to = 'images/', null=True, blank=True )
    image5 = models.ImageField(upload_to = 'images/', null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.profession)
        super(Service,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.profession

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
