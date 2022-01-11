from django.shortcuts import render, HttpResponseRedirect
from core.models import User, FooterUpload

from django.contrib import messages
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'save_editdetail_btn' in request.POST:
            print(request.POST)
            print(request.user)
            candidate = User.objects.filter(username=request.user)
            candidate.update(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                mobile=request.POST['mobile'],
                address=request.POST['address'],
                state=request.POST['state'],
                country=request.POST['country']
            )

            userdetail = User.objects.get(username=request.POST['username'])

        else:

            userdetail = User.objects.get(username=request.user)
        footer_data = footer_info()
        return render(request, 'core/profile.html', {'user_detail': userdetail, 'footer_context': footer_data})
    else:
        return HttpResponseRedirect("/")


# def edit_Profile(request):
#    if request.user.is_authenticated:
#        if request.method=='POST':


def update_profile_img(request):
    if request.method == "POST" and "update_profile_img_btn" in request.POST:
        print(request.FILES['profile_img'])
        # print(request.FILES)
        candidate = User.objects.filter(username=request.user)
        candidate.update(photo=request.FILES['profile_img'])
    return HttpResponseRedirect("/profile/")


def footer_info():
    footer_data = FooterUpload.objects.all()
    footer_context = footer_data
    return footer_context
