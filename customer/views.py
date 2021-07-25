from product.models import Product, ProductImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.db import transaction

from django.shortcuts import render, redirect
from .models import Customer, CustomerImage, Review
from vendor.models import User,VendorImage, Vendor
from lab.models import Lab, LabImage
from doctor.models import DoctorImage, Doctor, DoctorAppointment
from .forms import LoginForm, CustomerForm, CustomerImageForm
from order.models import Order,OrderItem

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
@login_required
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
def doctorAppointmentList(request):
    try:
        context = {
                    'topic':'Dashboard',
                    'account': 'Home',
                    'recent_page': 'Appointment List',
                    }

        appointment_list = DoctorAppointment.objects.filter(customer=Customer.objects.get(user=request.user)) 
        paginator = Paginator(appointment_list, 1)

        page_number = request.GET.get('page')
        appointments = paginator.get_page(page_number)
        
        return render(request, 'customer/doctor-appointment-list.htm',{'context':context, 'appointments': appointments})
    except e:
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
    print('here')
    context={
    'topic':'Dashboard',
    'account': 'Home',
    'recent_page': 'Order List',
    }

    orders_list = Order.objects.filter(customer=Customer.objects.get(user=request.user)) 
    orders_objects = OrderItem.objects.filter(order__customer=Customer.objects.get(user=request.user)) 
    paginator = Paginator(orders_list, 10)

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    return render(request, 'customer/order.htm', {'context' : context, 'orders': orders, 'order_items' : orders_objects})

@login_required
def appointment(request):
    context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Lab appointment List',
                }
    return render(request, 'customer/appointment.htm', {'context' : context})    

@login_required
def customerLogout(request):
    logout(request)
    return redirect('/')

@login_required
def doctor(request):
    try:
        context = {
                    'topic': 
                    'Online Doctor Consultation',
                    'account': 'Home',
                    'recent_page': 'Doctor Consultation',
                    }
        doctor_img_list= DoctorImage.objects.all()
        paginator = Paginator(doctor_img_list, 10)

        page_number = request.GET.get('page')
        doctor_img = paginator.get_page(page_number)
        
        return render(request,'customer/doctor.htm',{'context' : context, 'doctor_img' : doctor_img})
    except:
        return render(request,'product/shop/')

@login_required
def vendors(request):
    try:
        context = {
                    'topic':'Vendors',
                    'account': 'Vendor',
                    'recent_page': 'Vendor List',
                    }

        vendor_img_list = VendorImage.objects.filter(img_type="profile")
        paginator = Paginator(vendor_img_list, 10)

        page_number = request.GET.get('page')
        vendor_img = paginator.get_page(page_number)

        return render(request,'customer/vendors.htm',{'context' : context, 'vendor_img' : vendor_img})
    except:
        return render(request,'product/shop/')

@login_required
def vendorDetails(request,id):
    try:
        vendor = Vendor.objects.get(id=id)
        vendor_img = VendorImage.objects.get(img_type="profile", vendor=id)
        products = ProductImage.objects.filter(vendor=id, main=True)

        return render(request,'customer/vendor-details.htm',{'vendor':vendor, 'vendor_img': vendor_img , 'products' : products})
    except:
        return render(request,'product/shop/')

@login_required
def lab(request):
    try:
        context = {
                    'topic':'Lab',
                    'account': 'lab',
                    'recent_page': 'Lab List',
                    }

        lab_img = LabImage.objects.filter(img_type="profile")

        return render(request,'customer/lab.htm',{'context' : context, 'lab_img' : lab_img})
    except:
        return render(request,'service/shop/')

@login_required
def labDetails(request,id):
    try:
        print(id)
        lab = Lab.objects.get(id=id)
        lab_img = LabImage.objects.get(img_type="profile", lab=id)
        # products = ProductImage.objects.filter(lab=id, main=True)

        return render(request,'customer/lab-details.htm',{'lab':lab, 'lab_img': lab_img})
    except:
        return render(request,'service/shop/') 

@login_required
@transaction.atomic
def addReview(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        message =""

        if request.method=="POST":
            if(request.POST.get('review')!=""):
                customer = Customer.objects.filter(user=request.user).first()
                customerImage = CustomerImage.objects.get(customer=customer)
                product = Product.objects.get(id=id)
               
                Review.objects.create(
                    customer = customer,
                    image = customerImage,
                    product = product,
                    description = request.POST.get('review'),
                )

                return redirect('/product/shop/detail/{0}'.format(id))
                
            else:
                message = "Review cannot be empty."


        product = Product.objects.get(id=id)
        product_img = ProductImage.objects.filter(product=product)
        reviews = Review.objects.filter(product=product)

        return render(request,'product/customer_detail.htm', {'context' : context,'product': product, 'product_img' : product_img, 'message':message, 'reviews':reviews})
    except e:
        print(e)
        return redirect('/product/shop/')


   
