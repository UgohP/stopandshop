from django.db import models
from users.models import *

# Create your models here.

class Electronic(models.Model):
    negotiate = [
        ('Negotiable', 'Negotiable'),
        ('Unnegotiable', 'Unnegotiable'),
    ]
    electronics_vendor = models.ForeignKey(Vendor, related_name='electronics_vendors', on_delete=models.CASCADE, null=True)
    electronics_name = models.CharField(max_length=50)
    electronics_price = models.FloatField()
    haggle = models.CharField(max_length=50, choices=negotiate, default='Negotiable')
    slug = models.SlugField(null=True, blank=True)
    electronics_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/', null=True)
    image2 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image3 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image4 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    image5 = models.ImageField(upload_to = 'images/', null=True, blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.electronics_name)
        super(Electronic,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.electronics_name

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

