from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'medicalapp/index.htm')

def doctor(request):
    return render(request, 'medicalapp/doctor.htm')

def shop(request):
    return render(request, 'medicalapp/shop.htm')

def login(request):
    return render(request, 'medicalapp/login.htm')

def signin(request):
    return render(request, 'medicalapp/signin.htm')

def dashboard(request):
    return render(request, 'medicalapp/dashboard.htm')

def order(request):
    return render(request, 'medicalapp/order.htm')

def address(request):
    return render(request, 'medicalapp/address.htm')

def profileDetails(request):
    return render(request, 'medicalapp/profile-details.htm')

def forgetPassword(request):
    return render(request, 'medicalapp/forget-password.htm')

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
    

