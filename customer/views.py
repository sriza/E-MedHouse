from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'customer/dashboard.htm')

def login(request):
    return render(request, 'customer/login.htm')

def signin(request):
    return render(request, 'customer/signin.htm')

def order(request):
    return render(request, 'customer/order.htm')

def address(request):
    return render(request, 'customer/address.htm')

def profileDetails(request):
    return render(request, 'customer/profile-details.htm')

def forgetPassword(request):
    return render(request, 'customer/forget-password.htm')