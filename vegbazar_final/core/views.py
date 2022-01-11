from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, reverse
from core.models import ImageSlider, FooterUpload, User, Order, SemiImageSlider, Profile, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Products.models import Product
from django.views.generic.base import RedirectView
from .helpers import send_forget_password_mail
from Products.views import add_to_cart
import string
import random
import uuid


def indexpage(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
    if request.method == 'POST' and 'signup_submit_btn' in request.POST:

        users = User.objects.all()

        for x in users:
            if x.username == request.POST['uname']:
                return HttpResponse('<h3>duplicate entry not allowed</h3><hr><h2> Change Your username</h2>')
        myuser = User.objects.create_user(username = request.POST['uname'], password=request.POST['pass'],
                                          email=request.POST['email'], mobile = request.POST['mobile'])

        myuser.save()

        messages.success(request, 'signed up successfully...!')
        footer_context = footer_info()
        return render(request, 'core/veg_login.html', {'footer_context': footer_context})

    slider = ImageSlider.objects.all()
    semi_slider = SemiImageSlider.objects.all()
    top_deals = Product.objects.filter(is_top_deal=True)
    print("top_deals :", top_deals)
    footer_context = footer_info()
    return render(request, 'core/index.html', {'slider': slider, 'top_deals': top_deals,
                                               'footer_context': footer_context, 'semi_slider': semi_slider})


def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST' and 'login_btn' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(request.user)
                print(user)
                login(request, user)
                print(request.user)

                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'invalid credentials...!')

        footer_context = footer_info()
        return render(request, 'core/veg_login.html', {'footer_context': footer_context})

    else:
        return redirect('/')


def cartpage(request):
    if request.method == 'POST' and 'check_out_btn' in request.POST:
        # print('this is session =', request.session)
        print('this is inside cart')
        cart = request.session.get('cart')
        # print(cart)
        username = request.POST.get('username')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        # print(username)
        # print('this is in checkout')
        print(cart)
        # print(request.POST)
        product_ids = list(cart.keys())
        carted_products = Product.objects.filter(id__in=product_ids)
        print('carted_products :', carted_products)

        for item in carted_products:
            print(item.product_name)
            print(cart.keys())
            print("required quantity:", type(cart.get(str(item.id))))
            print("product price : ", item.product_price)
            print('available quantity :', item.product_available_quantity,
                  type(item.product_available_quantity))
            if (int(item.product_available_quantity) < int(cart.get(str(item.id)))):
                footer_context = footer_info()
                ids = list(request.session.get('cart').keys())
                carted_products = Product.objects.filter(id__in=ids)

                my_warning = "Required quantity is not available for {}...!".format(
                    item.product_name)

                messages.add_message(request, messages.WARNING, my_warning)
                
                return render(request, 'core/cart.html', {'footer_context': footer_context, 'carted_products': carted_products})

            Order(product_img=item.product_img, product_id=item.id,
                  product_name=item.product_name, product_price=item.product_price,
                  user_name=username, address=address, mobile=mobile,
                  quantity=cart.get(str(item.id)),
                  total_price=(int(cart.get(str(item.id))) * int(item.product_price))).save()

            Product.objects.filter(product_name=item.product_name).update(
                product_available_quantity=item.product_available_quantity-int(cart.get(str(item.id))))

        

        print('Placed Order...!')
        request.session['cart'] = {}
        my_success = "Congratulations Your order is placed..!"

        messages.add_message(request, messages.SUCCESS, my_success)
        return redirect('cartpage')

    cart = request.session.get('cart')
    print(cart)
    if cart != None:
        print(request.session.get('cart'))
        ids = list(request.session.get('cart').keys())
        carted_products = Product.objects.filter(id__in=ids)
        print('carted_products:', carted_products)
        footer_context = footer_info()
        return render(request, 'core/cart.html', {'carted_products': carted_products, 'footer_context': footer_context})
    else:
        messages.add_message(request, messages.WARNING, "You are not logged in...!")
        return redirect('cartpage')

def removeItem(request, id):
    context = {}
    #if request.method == "POST":

    print(request.session)
        # print(request.session.cart)
    cart = request.session.get('cart')
    print("cart=", cart)
    item_ids = list(cart.keys())
    print("ids=", item_ids)
    id = str(id)
        #cart.pop(product_id)
    cart.pop(id)
    request.session['cart']=cart

    context['footer_context'] = footer_info()
    return redirect('cartpage')
    #return HttpResponseRedirect('/cartpage/')

def quantityManager(request):
    if request.method=='POST':
        cart = request.session.get('cart')
        add_to_cart(request,cart)
    return redirect('cartpage')  




def search(request):
    query = request.GET['query']
    print('query : ', query)
    search_results = None
    if len(query.strip()) > 0:
        search_results = Product.objects.filter(product_name__icontains=query)
        print('search_results :', search_results)
    # print(search_results.product_name)
    footer_context = footer_info()
    return render(request, 'core/search_result.html', {'search_results': search_results,
                                                       'query': query, 'footer_context': footer_context})


def footer_info():
    footer_data = FooterUpload.objects.all()
    footer_context = footer_data
    return footer_context


def aboutus_page(request):
    footer_data = footer_info()
    return render(request, 'core/aboutus_page.html', {'footer_context': footer_data})


def offer_page(request):
    print("-----Offer Page-----")
    order_status = Order.objects.all()
    temp = False
    offer = None
    for x in order_status:
        if x.user_name == request.user:
            temp = True
    if temp == False:
        offers = Offer.objects.all()
        print(offer)

    print('order_status : ', order_status)

    footer_context = footer_info()
    return render(request, 'core/offers.html', {'footer_context': footer_context, 'offers': offers})


def order_Page(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
    footer_context = footer_info()
    orders = Order.objects.filter(
        user_name=request.user).order_by('order_date').reverse()

    return render(request, 'core/orders.html', {'orders': orders, 'footer_context': footer_context})


def Logout(request):
    # del request.session['cart']
    #    print(request.session)
    #    request.session.clear()
    #    print(request.session)
    logout(request)
#    print(request.session)
    return HttpResponseRedirect('/')


def changePassword(request):
    context = {}
    ch = User.objects.filter(id=request.user.id)
    if len(ch) > 0:
        data = User.objects.get(id=request.user.id)
        context["data"] = data
    if request.method == "POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]

        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request, user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    footer_context = footer_info()
    context['footer_context'] = footer_context
    return render(request, "core/ChangePassword.html", context)


def forgetPassword(request):
    context = {}
    if request.method == "POST" and 'send_uname_btn' in request.POST:
        username = request.POST.get('send_uname')
        print("Username : ", username)
        if not User.objects.filter(username=username).first():
            context['col'] = "alert-warning"
            context['msz'] = "This is not a valid username..!"
        else:
            user_obj = User.objects.get(username=username)
            print("User object : ", user_obj)
            recipient_mail = user_obj.email
            print("User Email : ", recipient_mail)
            token = str(uuid.uuid4())
            user_obj.forget_password_token = token
            user_obj.save()
            send_forget_password_mail(recipient_mail, token)
            context['col'] = "alert-success"
            context['msz'] = "A mail is sent on your registered Email id...!"

    footer_context = footer_info()
    context['footer_context'] = footer_context
    return render(request, 'core/ForgetPassword.html', context)



def resetPassword(request, token):
    context = {}
    try:
        user_obj = User.objects.filter(forget_password_token=token).first()
        context['user_id'] = user_obj.id

        print("User object : ", user_obj)
        print(user_obj.id)

        if request.method == 'POST':
            new_password = request.POST.get('new_pass')
            confirm_password = request.POST.get('confirm_pass')
            user_id = request.POST.get('user_id')

            if user_id is None:
                context['msz'] = "No user id found"

            if user_id is not None:
                user_obj.set_password(new_password)
                user_obj.save()
                return redirect('/login/')

    except Exception as e:
        print(e)
    footer_context = footer_info()
    context['footer_context'] = footer_context
    return render(request, "core/ResetPassword.html", context)




def contact(request):
    context = {}
    if request.method == "POST" and "contact_send_btn" in request.POST:
        Contact(email=request.POST['contact_email'],
                message=request.POST['contact_msg']).save()
        context['message'] = 'message sent'
        context['color'] = 'alert-success'
    else:
        context['message'] = 'message not sent'
        context['color'] = "alert-danger"
    context['slider'] = ImageSlider.objects.all()
    context['semi_slider'] = SemiImageSlider.objects.all()
    context['top_deals'] = Product.objects.filter(is_top_deal=True)
#    print("top_deals :", top_deals)
    context['footer_context'] = footer_info()
    return render(request, 'core/index.html', context)
