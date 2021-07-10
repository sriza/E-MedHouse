from product.models import Product, ProductImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.db import transaction

from django.shortcuts import render, redirect
from .models import Doctor, DoctorImage
from vendor.models import User,VendorImage, Vendor
from .forms import LoginForm, doctorForm, DoctorImageForm

from django.shortcuts import render

# Create your views here.

def doctorLogin(request):
    if request.user.is_authenticated and request.user.role==3:

        return redirect('/doctor/dashboard/')
    else:
        form = LoginForm(request.POST or None)

        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/doctor/dashboard/')

        return render(request, 'doctor/login.htm',{'form':form})

@transaction.atomic
def signin(request):
    form    = doctorForm(request.POST or None, request.FILES or None)
    img_form = DoctorImageForm(request.POST or None, request.FILES or None)

    if form.is_valid() and img_form.is_valid():
        try :
            e = request.POST.get("email")
            p = request.POST.get("password")

            user = User.objects.create(email=e, password=p, role=3)
            user.set_password(p)
            user.save()

            doctor = form.save(commit=False)
            doctor.user = user
            doctor.save()

            img             = img_form.save(commit=False)
            img.doctor    = doctor
            img.description = request.POST.get("full_name")
            img.save()
    
            return HttpResponseRedirect('/doctor/login/')
    
        except e:
            print(e)
            return render(request,'medicalapp/index.htm')

    return render(request,'doctor/signin.htm',{'form':form, 'img_form':img_form })

@transaction.atomic
def dashboard(request):
    try :
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'My Account',
                }

        doctor = Doctor.objects.get(user=request.user)
        doctor_img = DoctorImage.objects.get(doctor=doctor)

        return render(request, 'doctor/dashboard.htm', {'context':context, 'doctor': doctor, 'doctor_img' :doctor_img } )
    except:
        return render(request,'medicalapp/index.htm')



@login_required
def profileDetails(request):
    try:
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'My Profile',
                    }

        # edit_form  = RegisterForm(request.POST or None)

        doctor = Doctor.objects.get(user=request.user)
        doctor_img = DoctorImage.objects.get(doctor=doctor)

        return render(request, 'doctor/profile-details.htm',{'context':context, 'doctor': doctor, 'doctor_img' :doctor_img})
    except:
        return render(request,'medicalapp/index.htm')


@login_required
def order(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Order List',
}
    return render(request, 'doctor/order.htm', {'context' : context})

@login_required
def doctorLogout(request):
    logout(request)
    return redirect('/')


def forgetPassword(request):
    return render(request,'doctor/forget-password.htm')








    
