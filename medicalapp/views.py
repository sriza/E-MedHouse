from django.shortcuts import render
from product.models import ProductImage

# Create your views here.
def index(request):
    images = ProductImage.objects.filter(main= True)[:9]

    return render(request, 'medicalapp/index.htm', {'images' : images})

def doctor(request):
    context={
    'topic':'Online Doctors Appointment Request',
    'account': 'Home',
    'recent_page': 'Doctor Consultation',
    }
    return render(request, 'medicalapp/doctor.htm',{'context' : context})

def vendors(request):
    context={
    'topic':'Online Doctors Appointment Request',
    'account': 'Home',
    'recent_page': 'Doctor Consultation',
    }
    return render(request, 'medicalapp/vendors.htm',{'context' : context})

def shop(request):
    return render(request, 'medicalapp/shop.htm')

def cart(request):
    return render(request, 'medicalapp/cart.htm')

def checkout(request):
    return render(request, 'medicalapp/checkout.htm')

def confirmation(request):
    return render(request, 'medicalapp/confirmation.htm')

def contact(request):
    return render(request, 'medicalapp/contact.htm')

def shopslider(request):
    return render(request, 'medicalapp/shop-sidebar.htm')
    

