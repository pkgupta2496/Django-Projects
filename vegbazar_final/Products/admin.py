from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_img','product_available_quantity',
                  'is_product_veg','is_product_fruit','is_top_deal']

