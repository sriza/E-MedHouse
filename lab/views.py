from service.models import Appointment, LabAppointment, Service
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import transaction
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Lab, LabImage
from vendor.models import User
from .forms import LoginForm, RegisterForm, RegistrationImageForm, UpdateRegisterForm, RegistrationImageEditForm
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
        lab = Lab.objects.get(user=request.user)
        lab_img = LabImage.objects.get(lab=lab, img_type='profile')

        if request.method == "POST" :
            title = request.POST.get('title')
            print(title)
          
            if title:
                services_list = Service.objects.filter((Q(title__contains = title)| Q(appointment_date__contains = title)| Q(meta_title__contains = title)| Q(service_type__contains = title))& Q(lab=lab))
            else :
                services_list = Service.objects.filter(lab=lab)
        
        else :
                services_list = Service.objects.filter(lab=lab)
            
        paginator = Paginator(services_list, 10)

        page_number = request.GET.get('page')
        services = paginator.get_page(page_number)

        return render(request, 'lab/dashboard.htm', {'context':context, 'lab': lab, 'lab_img' : lab_img, 'services' : services})
    except :
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
def forgetPassword(request):
    return render(request, 'lab/forget-password.htm')

@login_required
def appointment(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Appointment List',
    }

    if request.method == "POST" :
        title = request.POST.get('title')
        
        if title:
            appointments_list = Appointment.objects.filter((Q(full_name__contains = title)| Q(contact__contains = title)| Q(service__meta_title__contains = title)| Q(service__service_type__contains = title)) & Q(lab=Lab.objects.get(user=request.user)))
        else :
            appointments_list = Appointment.objects.filter(lab=Lab.objects.get(user=request.user))
            
    else :
        appointments_list = Appointment.objects.filter(lab=Lab.objects.get(user=request.user))
            
    paginator = Paginator(appointments_list, 10)

    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)

    return render(request, 'lab/appointment.htm', {'context' : context, 'appointments' : appointments })    

@login_required
def labLogout(request):
    logout(request)
    return redirect('/')    


@login_required
@transaction.atomic
def updateLab(request,id):
    object        = Lab.objects.get(id=id) 
    form          = UpdateRegisterForm(instance=object, data=request.POST or None)
    profile_form  = RegistrationImageEditForm(request.FILES or None)
    image         = LabImage.objects.get(lab=object, img_type="profile")

    if form.is_valid() :
        try : 
            form.save()
            image = request.FILES.get('image')

            if bool(image) :
                LabImage.objects.filter(lab=object, img_type="profile").delete()

                profile             = profile_form.save(commit=False)
                profile.lab         = object
                profile.description = request.POST.get("business_name")
                profile.img_type    = 'profile'
                profile.save()

            return redirect('/lab/profile-details/')
        except:
            return redirect('/lab/dashboard/')

    return render(request,'lab/updatelab.htm', {'form' : form, 'lab':object, 'profile_form' : profile_form, 'image':image})

