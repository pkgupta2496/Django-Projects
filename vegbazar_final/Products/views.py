from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.
from django.contrib import messages

from core.models import FooterUpload


def vegpage(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        #('this is get request inside vegpage')
        #("**********************")
    if request.method == 'POST':
        print('#######################')
        print('This is data of request.POST', request.POST)
        # cart=request.session.get('cart')
        cart = request.session.setdefault('cart', {})
        print('cart before adding product : ', cart)
        #print('product id : ',product_id)
        #quantity = cart[product_id]

        username = request.POST['username']
        print(username)
        if username != 'AnonymousUser':
            add_to_cart(request, cart)
        else:
            messages.warning(request, "you are not logged in...!")
            footer_context = footer_info()

            return render(request, "core/veg_login.html", {'footer_context': footer_context})

        # cart[product_id]=quantity
        # if 'decrease_quantity' in request.POST:
        #   add_to_cart(request,product_id,True)

    # if request.method=='POST' and 'decrease_quantity_btn' in request.POST:
    #    product_id = request.POST['product_id']
    footer_context = footer_info()
    veg_product = Product.objects.filter(is_product_veg=True)
    return render(request, 'core/vegetable.html', {'veg_product': veg_product, 'footer_context': footer_context})


def add_to_cart(request,cart):
    product_id = request.POST.get('product_id')
    if 'add_to_cart_btn' in request.POST or 'increase_quantity_btn' in request.POST:
        if product_id in cart.keys():
            cart[product_id] = cart[product_id]+1
        else:
            cart[product_id] = 1
        print('yes')
    elif 'decrease_quantity_btn' in request.POST:
        if product_id in cart.keys():
            cart[product_id] = cart[product_id]-1

        if cart[product_id] < 1:
            cart.pop(product_id)

    request.session['cart'] = cart
    print('cart after adding product : ', cart)
     

def fruitpage(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        print('this is get request inside vegpage')

    if request.method == 'POST':
        print('#######################')
        print('This is data of request.POST', request.POST)
        # cart=request.session.get('cart')
        cart = request.session.setdefault('cart', {})
        print('cart before adding product : ', cart)
        #print('product id : ',product_id)
        #quantity = cart[product_id]

        username = request.POST['username']
        print(username)
        if username != 'AnonymousUser':
            add_to_cart(request, cart)
        else:
            messages.warning(request, "you are not logged in...!")
            footer_context = footer_info()

            return render(request, "core/veg_login.html", {'footer_context': footer_context})

    footer_context = footer_info()
    fruit_product = Product.objects.filter(is_product_fruit=True)
    return render(request, 'core/fruit.html', {'fruit_product': fruit_product, 'footer_context': footer_context})


def footer_info():
    footer_data = FooterUpload.objects.all()
    return footer_data
