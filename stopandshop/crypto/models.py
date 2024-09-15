from django.db import models
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from users.models import *

# Create your models here.
class Crypto(models.Model):
    crypto_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to = 'images/', null=True, blank=True )
    discription = models.TextField(blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url