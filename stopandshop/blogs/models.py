from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
from users.models import *

# Create your models here.


class Blog(models.Model):
    posted_by = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=30, null=True)
    text = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    business_whatsapp_number = models.CharField(max_length=100, null=True) 
    blog_image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    blog_image2 = models.ImageField(upload_to = 'images/', null=True, blank=True)
    blog_image3 = models.ImageField(upload_to = 'images/', null=True, blank=True)
    blog_image4 = models.ImageField(upload_to = 'images/', null=True, blank=True)
    blog_image5 = models.ImageField(upload_to = 'images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)    

    def __str__(self):
        return str(self.posted_by).capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Blog,self).save(*args, **kwargs)
 
    @property
    def imageURL(self):
        try:
            url = self.blog_image.url
        except:
            url = ''
        return url

    @property
    def image2URL(self):
        try:
            url = self.blog_image2.url
        except:
            url = ''
        return url

    @property
    def image3URL(self):
        try:
            url = self.blog_image3.url
        except:
            url = ''
        return url

    @property
    def image4URL(self):
        try:
            url = self.blog_image4.url
        except:
            url = ''
        return url

    @property
    def image5URL(self):
        try:
            url = self.blog_image5.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ('-created',)


class BlogVideo(models.Model):
    posted_by = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=30, null=True)
    text = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    business_whatsapp_number = models.CharField(max_length=100, null=True) 
    blog_video = models.FileField(upload_to = 'videos/', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)    

    def __str__(self):
        return str(self.posted_by).capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(BlogVideo,self).save(*args, **kwargs)

    @property
    def videoURL(self):
        try:
            url = self.blog_video.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ('-created',)
