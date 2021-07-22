from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import transaction

from .models import Lab, LabImage
from vendor.models import User
from .forms import LoginForm, RegisterForm, RegistrationImageForm
from product.models import Product
from datetime import date, datetime

# Create your views here.


def labLogin(request):
    if request.user.is_authenticated and request.user.role==1:
        return redirect('/lab/dashboard/')
    else:
        form = LoginForm(request.POST or None)

        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/lab/dashboard/')

        return render(request, 'lab/login.htm',{'form':form})

@transaction.atomic
def signin(request):
    register_form    = RegisterForm(request.POST or None)
    citizenship_form = RegistrationImageForm(request.POST or None, request.FILES or None)
    pancard_form     = RegistrationImageForm(request.POST or None, request.FILES or None)
    license_form     = RegistrationImageForm(request.POST or None, request.FILES or None)
    profile_form     = RegistrationImageForm(request.POST or None, request.FILES or None)

    if register_form.is_valid() and citizenship_form.is_valid() and pancard_form.is_valid() and license_form.is_valid() and profile_form.is_valid():
        try :
            e = request.POST.get("email")
            p = request.POST.get("password")

            user = User.objects.create(
                email=e, password=p, role=1
            )

            user.set_password(p)
            user.save()

            lab = register_form.save(commit=False)
            lab.user = user
            lab.save()

            citizenship             = citizenship_form.save(commit=False)
            citizenship.lab         = lab
            citizenship.description = request.POST.get("full_name")
            citizenship.img_type    = 'citizenship'
            citizenship.save()

            pancard             = pancard_form.save(commit=False)
            pancard.lab         = lab
            pancard.description = "PAN Card"
            pancard.img_type    = 'pan'
            pancard.save()

            license             = license_form.save(commit=False)
            license.lab         = lab
            license.description = "Government Based Pharmacy Registration License"
            license.img_type    = 'license'
            license.save()

            profile             = profile_form.save(commit=False)
            profile.lab         = lab
            profile.description = request.POST.get("business_name")
            profile.img_type    = 'profile'
            profile.save()
    
            return HttpResponseRedirect('/lab/login/')
    
        except e:
            print(e)
            return render(request,'medicalapp/index.htm')

    return render(request, 
                'lab/signin.htm',
                {
                'register_form':register_form,
                'citizenship_form':citizenship_form,
                'pancard_form':pancard_form,
                'license_form':license_form,
                'profile_form':profile_form})

@transaction.atomic
def dashboard(request):
    try :
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'My Account',
                }
        lab     = Lab.objects.get(user=request.user)
        print(lab)
        lab_img = LabImage.objects.get(lab=lab, img_type='profile')
        print(lab_img)

        # expiry = Product.objects.filter(lab=lab, expiry_date__lt=datetime.today())
        # finishing = Product.objects.filter(lab=lab, quantity__lt = 5)

        return render(request, 'lab/dashboard.htm', {'context':context, 'lab': lab, 'lab_img' : lab_img})
    except e:
        print(e)
        return render(request,'medicalapp/index.htm')

@login_required
def profileDetails(request):
    try:
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'My Profile',
                    }

        edit_form  = RegisterForm(request.POST or None)

        lab     = Lab.objects.get(user=request.user)
        lab_img = LabImage.objects.get(lab=lab, img_type='profile')

        return render(request, 'lab/profile-details.htm',{'context':context, 'lab': lab, 'lab_img': lab_img})
    except:
        return render(request,'medicalapp/index.htm')

@login_required
def serviceDetails(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Service',
    }
    return render(request, 'lab/service-details.htm', context)       

@login_required
def forgetPassword(request):
    return render(request, 'lab/forget-password.htm')

# @login_required
# def order(request):
#     return render(request, 'lab/order.htm')

@login_required
def appointment(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Appointment List',
}
    return render(request, 'lab/appointment.htm', {'context' : context})    

@login_required
def address(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Address',
}
    return render(request, 'lab/address.htm', {'context': context})

@login_required
def labLogout(request):
    logout(request)
    return redirect('/')    
