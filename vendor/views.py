from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'vendor/dashboard.htm')

def login(request):
    return render(request, 'vendor/login.htm')

def signin(request):
    return render(request, 'vendor/signin.htm')

def order(request):
    return render(request, 'vendor/order.htm')

def address(request):
    return render(request, 'vendor/address.htm')

def profileDetails(request):
    return render(request, 'vendor/profile-details.htm')

def productDetails(request):
    return render(request, 'vendor/product-details.htm')

def viewProductDetails(request):
    return render(request, 'vendor/view-product-details.htm')

def forgetPassword(request):
    return render(request, 'vendor/forget-password.htm')