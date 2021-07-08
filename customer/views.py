from product.models import Product, ProductImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.db import transaction

from django.shortcuts import render, redirect
from .models import Customer, CustomerImage
from vendor.models import User,VendorImage, Vendor
from .forms import LoginForm, CustomerForm, CustomerImageForm

from django.shortcuts import render

# Create your views here.

def customerLogin(request):
    if request.user.is_authenticated and request.user.role==2:

        return redirect('/customer/dashboard/')
    else:
        form = LoginForm(request.POST or None)

        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/customer/dashboard/')

        return render(request, 'customer/login.htm',{'form':form})

@transaction.atomic
def signin(request):
    form    = CustomerForm(request.POST or None, request.FILES or None)
    img_form = CustomerImageForm(request.POST or None, request.FILES or None)

    if form.is_valid() and img_form.is_valid():
        try :
            e = request.POST.get("email")
            p = request.POST.get("password")

            user = User.objects.create(email=e, password=p, role=2)
            user.set_password(p)
            user.save()

            customer = form.save(commit=False)
            customer.user = user
            customer.save()

            img             = img_form.save(commit=False)
            img.customer    = customer
            img.description = request.POST.get("full_name")
            img.save()
    
            return HttpResponseRedirect('/customer/login/')
    
        except e:
            print(e)
            return render(request,'medicalapp/index.htm')

    return render(request,'customer/signin.htm',{'form':form, 'img_form':img_form })

@transaction.atomic
def dashboard(request):
    try :
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'My Account',
                }

        customer = Customer.objects.get(user=request.user)
        customer_img = CustomerImage.objects.get(customer=customer)

        return render(request, 'customer/dashboard.htm', {'context':context, 'customer': customer, 'customer_img' :customer_img } )
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

        customer = Customer.objects.get(user=request.user)
        customer_img = CustomerImage.objects.get(customer=customer)

        return render(request, 'customer/profile-details.htm',{'context':context, 'customer': customer, 'customer_img' :customer_img})
    except:
        return render(request,'medicalapp/index.htm')

    
@login_required
def productDetails(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Product',
    }
    return render(request, 'customer/product-details.htm', context)

@login_required
def forgetPassword(request):
    return render(request, 'customer/forget-password.htm')

@login_required
def order(request):
    return render(request, 'customer/order.htm')
    

@login_required
def order(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Order List',
}
    return render(request, 'customer/order.htm', {'context' : context})

@login_required
def customerLogout(request):
    logout(request)
    return redirect('/')


def forgetPassword(request):
    return render(request,'customer/forget-password.htm')

def order(request):
    return render(request,'customer/order.htm')

def doctor(request):
    return render(request,'customer/doctor.htm')

def vendors(request):
    try:
        context = {
                    'topic':'Vendors',
                    'account': 'Vendor',
                    'recent_page': 'Vendor List',
                    }

        vendor_img = VendorImage.objects.filter(img_type="profile")

        return render(request,'customer/vendors.htm',{'context' : context, 'vendor_img' : vendor_img})
    except:
        return render(request,'product/shop/')

def vendorDetails(request,id):
    try:
        print(id)
        vendor = Vendor.objects.get(id=id)
        vendor_img = VendorImage.objects.get(img_type="profile", vendor=id)
        products = ProductImage.objects.filter(vendor=id, main=True)

        return render(request,'customer/vendor-details.htm',{'vendor':vendor, 'vendor_img': vendor_img , 'products' : products})
    except:
        return render(request,'product/shop/')
    
