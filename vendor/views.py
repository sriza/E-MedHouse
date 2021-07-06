
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context={
        'topic':'Dashboard',
        'account': 'Home',
        'recent_page': 'My Account',
    }
    return render(request, 'vendor/dashboard.htm', context)

def login(request):
    return render(request, 'vendor/login.htm')

def signin(request):
    return render(request, 'vendor/signin.htm')

def order(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Order List',
}
    return render(request, 'vendor/order.htm', context)

def address(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Address',
}
    return render(request, 'vendor/address.htm', context)

def profileDetails(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Profile',
}
    return render(request, 'vendor/profile-details.htm',context)

def productDetails(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Product',
}
    return render(request, 'vendor/product-details.htm', context)

def viewProductDetails(request):
    return render(request, 'vendor/view-product-details.htm')

def forgetPassword(request):
    return render(request, 'vendor/forget-password.htm')