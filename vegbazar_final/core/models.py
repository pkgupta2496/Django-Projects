from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to="myimage", default="No Img")
    user_id = models.IntegerField(unique=True, null=False, primary_key=True),
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=10)
    forget_password_token = models.CharField(max_length=100, null=True)


class ImageSlider(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


class SemiImageSlider(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_img = models.ImageField(upload_to='OrderImage')
    product_id = models.CharField(max_length=2, blank=False)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=10)
    quantity = models.IntegerField()
    total_price = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=10, blank=False)
    order_date=models.DateTimeField(auto_now=True)


class Offer(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='myimage', default=None)
    discount = models.CharField(max_length=10, default=None)


class FooterUpload(models.Model):
    about_us = models.TextField(blank=False)
    address = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=10)
    email = models.EmailField()


class Profile(models.Model):
   pass


class Contact(models.Model):
    email=models.EmailField()
    message = models.TextField()