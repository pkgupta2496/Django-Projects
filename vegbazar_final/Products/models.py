from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    product_price = models.CharField(max_length=50)
    product_img = models.ImageField(upload_to='myimage')
    product_available_quantity = models.IntegerField()
    is_product_veg =models.BooleanField()
    is_product_fruit = models.BooleanField()
    is_top_deal = models.BooleanField()

