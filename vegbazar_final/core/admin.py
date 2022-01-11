from django.contrib import admin
from .models import User, ImageSlider, Order, FooterUpload, SemiImageSlider, Offer, Profile, Contact
from django.contrib.auth.admin import UserAdmin
# Register your models here.


#admin.site.register(User, UserAdmin)
#UserAdmin.fieldsets += ('Custom fields set',
#                        {'fields': ('mobile', 'photo', 'address', 'state', 'country',)}),


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'mobile','photo','address','state','country']

# Register your models here.

@admin.register(ImageSlider)
class ImageSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']


@admin.register(SemiImageSlider)
class SemiImageSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_img', 'product_id',
                    'product_name', 'product_price', 'quantity',
                    'total_price', 'user_name', 'address', 'mobile']


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'discount']


@admin.register(FooterUpload)
class FooterUplodAdmin(admin.ModelAdmin):
    list_display = ['about_us', 'address', 'phone', 'email']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'message']


