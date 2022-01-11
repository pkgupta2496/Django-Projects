from django.contrib import admin
from django.urls import path

from core import views as core_views

from Products import views as product_views
from Profile import views as profile_views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('adminpanel/', core_views.RedirectView.as_view(url='/admin/'), name='adminpage'),
    # path('checkout/',core_views.checkout,name='checkout'),
    path('contact/', core_views.contact, name='contact'),
    path('logout/', core_views.Logout, name='logout'),
    path('cart/', core_views.cartpage, name='cartpage'),
    path('login/', core_views.loginpage, name='loginpage'),
    path('searchbox/', core_views.search, name='searchresult'),
    path('aboutus/', core_views.aboutus_page, name='aboutus'),
    path('offers/', core_views.offer_page, name='offer'),
    path('orders/', core_views.order_Page, name='orders'),
    path('core_views/', core_views.changePassword, name='changepass'),
    path('forget_pass/', core_views.forgetPassword, name='forgetpass'),
    path('reset_pass/<token>/', core_views.resetPassword, name="resetpass"),
    path('remove_item/<int:id>', core_views.removeItem, name="removeitem"),
    path('', core_views.indexpage, name='homepage'),
    
    
    path('vegpage/', product_views.vegpage, name='vegpage'),
    path('fruitpage/', product_views.fruitpage, name='fruitpage'),
    path('quantitymanager/', core_views.quantityManager,name='quantitymanager'),
    

    path('profile/', profile_views.profile, name='profile'),
    path('update_profile_img/', profile_views.update_profile_img,
         name='update_profile_img')

    

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
