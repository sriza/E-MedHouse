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

def lab(request):
    context={
    'topic':'Available laboratories',
    'account': 'Home',
    'recent_page': 'Lab',
    }
    return render(request, 'medicalapp/lab.htm',{'context' : context})

def shop(request):
    return render(request, 'medicalapp/shop.htm')

def cart(request):
    return render(request, 'medicalapp/cart.htm')

def checkout(request):
    return render(request, 'medicalapp/checkout.htm')

def confirmation(request):
    return render(request, 'medicalapp/confirmation.htm')

def contact(request):
    context={
    'topic':'Contact Us',
    'account': 'Home',
    'recent_page': 'contact',
    }
    return render(request, 'medicalapp/contact.htm',{'context' : context})

def about(request):
    context={
    'topic':'About Us',
    'account': 'Home',
    'recent_page': 'About Us',
    }
    return render(request, 'medicalapp/about-us.htm',{'context' : context})
    
def shopslider(request):
    return render(request, 'medicalapp/shop-sidebar.htm')
    

