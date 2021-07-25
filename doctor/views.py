from product.models import Product, ProductImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db import transaction
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Doctor, DoctorAppointment, DoctorImage
from customer.models import Customer
from vendor.models import User,VendorImage, Vendor
from .forms import LoginForm, doctorForm, DoctorImageForm, DoctorAppointmentForm, DoctorAppointmentEditForm


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
            img.doctor      = doctor
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

        doctor = Doctor.objects.get(user=request.user)
        doctor_img = DoctorImage.objects.get(doctor=doctor)

        return render(request, 'doctor/profile-details.htm',{'context':context, 'doctor': doctor, 'doctor_img' :doctor_img})
    except:
        return render(request,'medicalapp/index.htm')

@login_required
def doctorLogout(request):
    logout(request)
    return redirect('/')


def forgetPassword(request):
    return render(request,'doctor/forget-password.htm')

@login_required
def appointment(request,id):
    context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Appointment Booking Form',
                }

    form = DoctorAppointmentForm(request.POST or None)
    doctor_image = DoctorImage.objects.get(doctor__id=id)

    if form.is_valid() :
        try :
            appointment = form.save(commit=False)
            appointment.customer = Customer.objects.filter(user=request.user).first()
            appointment.doctor = Doctor.objects.get(id=id)
            appointment.save()

            return redirect('/doctor/payment/{0}/'.format(appointment.id))
    
        except e:
            return render(request,'customer/index.htm')    

    return render(request, 'doctor/doctor-appointment.htm', {'context' : context, 'form':form, 'doc_image':doctor_image}) 

@login_required
@transaction.atomic
def payment(request,id):
    appointment = DoctorAppointment.objects.get(id=id)
    doctor_image = DoctorImage.objects.get(doctor__id=appointment.doctor.id)

    return render(request,'doctor/payment.htm', {'doc_image':doctor_image, 'id':id} )


@login_required
@transaction.atomic
def paymentMade(request,id):
    try:
        DoctorAppointment.objects.filter(id=id).update(
            payment=True
        )
        
        return render(request,'medicalapp/appointment-confirmation.htm' )
    except:
        return redirect('/order/payment/'.id)

@login_required
@transaction.atomic
def cancelAppointment(request,id) :
    try :
        DoctorAppointment.objects.filter(id=id).delete()

        return redirect('/customer/doctor-appointment')
    except:
        return render(request,'customer/index.htm')  

@login_required
def appointmentList(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Appointment List',
    }
 
    appointment_list = DoctorAppointment.objects.filter(doctor=Doctor.objects.get(user=request.user), payment=True) 
    paginator = Paginator(appointment_list, 10)

    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)

    return render(request, 'doctor/order.htm', {'context' : context, 'appointments': appointments,'today' :timezone.now() })

@login_required
def updateAppointment(request,id):
    context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Appointment Booking Form',
                }
    object = DoctorAppointment.objects.get(id=id)        

    form = DoctorAppointmentEditForm(instance=object, data=request.POST or None)
    doctor_image = DoctorImage.objects.get(doctor__id=id)

    if form.is_valid() :
        try :
            DoctorAppointment.objects.filter(id=id).update(
                fixed_on = request.POST.get('fixed_on'),
                status = 'fixed'
            )

            return redirect('/doctor/appointmentList')
    
        except e:
            return render(request,'customer/index.htm')    

    return render(request, 'doctor/doctor-appointment-update.htm', {'context' : context, 'form':form, 'doc_image':doctor_image})

@login_required
@transaction.atomic
def statusCompleted(request,id):
    try:
        DoctorAppointment.objects.filter(id=id).update(
            status='completed'
        )
        
        return redirect('/doctor/appointmentList')
    except:
        return redirect('/doctor/appointmentList')



    
