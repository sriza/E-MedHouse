from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

from django.db import transaction
from product.models import Product, ProductImage
from django.shortcuts import render, redirect
from .models import User,Vendor, VendorImage
from .forms import LoginForm, RegisterForm, RegistrationImageForm, UpdateRegisterForm, RegistrationImageEditForm
from product.models import Product
from order.models import Order,OrderItem

from datetime import date, datetime

# Create your views here.

def vendorLogin(request):
    if request.user.is_authenticated and request.user.role==1:
        return redirect('/vendor/dashboard/')
    elif request.user.is_authenticated and request.user.role==3:
        return redirect('/vendor/dashboard/')
    else:
        form = LoginForm(request.POST or None)

        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/vendor/dashboard/')

        return render(request, 'vendor/login.htm',{'form':form})

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

            vendor = register_form.save(commit=False)
            vendor.user = user
            vendor.save()

            citizenship             = citizenship_form.save(commit=False)
            citizenship.vendor      = vendor
            citizenship.description = request.POST.get("full_name")
            citizenship.img_type    = 'citizenship'
            citizenship.save()

            pancard             = pancard_form.save(commit=False)
            pancard.vendor      = vendor
            pancard.description = "PAN Card"
            pancard.img_type    = 'pan'
            pancard.save()

            license             = license_form.save(commit=False)
            license.vendor      = vendor
            license.description = "Government Based Pharmacy Registration License"
            license.img_type    = 'license'
            license.save()

            profile             = profile_form.save(commit=False)
            profile.vendor      = vendor
            profile.description = request.POST.get("business_name")
            profile.img_type    = 'profile'
            profile.save()
    
            return HttpResponseRedirect('/vendor/login/')
    
        except e:
            print(e)
            return render(request,'medicalapp/index.htm')

    return render(request, 
                'vendor/signin.htm',
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
        vendor = Vendor.objects.get(user=request.user)
        print(vendor)
        vendor_img = VendorImage.objects.get(vendor=vendor, img_type='profile')
        print(vendor_img)

        expiry = Product.objects.filter(vendor=vendor, expiry_date__lt=datetime.today())
        finishing = Product.objects.filter(vendor=vendor, quantity__lt = 5)

        return render(request, 'vendor/dashboard.htm', {'context':context, 'vendor': vendor, 'vendor_img' : vendor_img, 'expiry' : expiry, 'finishing' : finishing})
    except :
        # print(e)
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

        vendor     = Vendor.objects.get(user=request.user)
        vendor_img = VendorImage.objects.get(vendor=vendor, img_type='profile')

        return render(request, 'vendor/profile-details.htm',{'context':context, 'vendor': vendor, 'vendor_img': vendor_img})
    except:
        return render(request,'medicalapp/index.htm')

    
@login_required
def productDetails(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Product',
    }
    return render(request, 'vendor/product-details.htm', context)

@login_required
def forgetPassword(request):
    return render(request, 'vendor/forget-password.htm')

@login_required
def order(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Order List',
    }
 
    if request.method == "POST" :
        title = request.POST.get('title')
        
        if title:
            orders_list = Order.objects.filter((Q(customer__full_name__contains = title)| Q(customer__contact_number__contains = title)) & Q(vendor=Vendor.objects.get(user=request.user)) & Q(payment=True)) 
        else :
            orders_list = Order.objects.filter(vendor=Vendor.objects.get(user=request.user), payment=True) 
    
    else :
        orders_list = Order.objects.filter(vendor=Vendor.objects.get(user=request.user), payment=True) 
    
    orders_objects = OrderItem.objects.filter(order__vendor=Vendor.objects.get(user=request.user)) 
    paginator = Paginator(orders_list, 10)

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    return render(request, 'vendor/order.htm', {'context' : context, 'orders': orders, 'order_items' : orders_objects})

@login_required
def address(request):
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'My Address',
    }

    return render(request, 'vendor/address.htm', {'context': context})

@login_required
def vendorLogout(request):
    logout(request)
    return redirect('/')
    

@login_required
@transaction.atomic
def updateVendor(request,id):
    object        = Vendor.objects.get(id=id) 
    form          = UpdateRegisterForm(instance=object, data=request.POST or None)
    image         = VendorImage.objects.get(vendor=object, img_type="profile")
    profile_form  = RegistrationImageEditForm(instance=image, data=request.FILES or None)

    if form.is_valid() :
        try : 
            form.save()

            image = request.FILES.get('image')

            if bool(image) :
                # VendorImage.objects.filter(vendor=object, img_type="profile").delete()

                # profile             = profile_form.save(commit=False)
                # profile.vendor      = object
                # profile.description = request.POST.get("business_name")
                # profile.img_type    = 'profile'
                profile_form.save()

            return redirect('/vendor/profile-details/')
        except:
            return redirect('/vendor/dashboard/')

    return render(request,'vendor/updatevendor.htm', {'form' : form, 'vendor':object, 'profile_form' : profile_form, 'image':image})

