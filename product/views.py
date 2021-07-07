from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required
from django.db import transaction
 

from django.shortcuts import redirect, render
from .forms import MedicineForm, DeviceForm, HygenicProductForm , ProductImageForm
from .models import Product, ProductImage
from vendor.models import Vendor
# Create your views here.

@login_required
@transaction.atomic
def createMedicine(request):
    form     = MedicineForm(request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product = form.save(commit=False)
            product.vendor = Vendor.objects.filter(user=request.user).first()
            product.product_type = request.POST.get('product_type')
            product.save()

            images = request.FILES.getlist('image')

            for image in images:
                img  = ProductImage.objects.create(
                        vendor      = Vendor.objects.filter(user=request.user).first(),
                        main        = main,
                        product     = product,
                        image       = image,
                        description = request.POST.get("title")
                    )
                main = False
            return redirect('/product/list/')
        except e:
            print(e);
            return redirect('/product/list/')

    return render(request,'product/medicine.htm', {'form' : form, 'img_form' : img_form})

@login_required
@transaction.atomic
def createDevice(request):
    form     = DeviceForm(request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product = form.save(commit=False)
            product.vendor = Vendor.objects.filter(user=request.user).first()
            product.product_type = request.POST.get('product_type')
            product.save()

            images = request.FILES.getlist('image')

            for image in images:
                img  = ProductImage.objects.create(
                        vendor      = Vendor.objects.filter(user=request.user).first(),
                        main        = main,
                        product     = product,
                        image       = image,
                        description = request.POST.get("title")
                    )
                main = False

            return redirect('/product/list/')
        except e:
            print(e);
            return redirect('/product/list/')

    return render(request,'product/device.htm', {'form' : form, 'img_form' : img_form})

@login_required
@transaction.atomic
def createHygenicProduct(request):
    form     = HygenicProductForm(request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product = form.save(commit=False)
            product.vendor = Vendor.objects.filter(user=request.user).first()
            product.product_type = request.POST.get('product_type')
            product.save()
          
            images = request.FILES.getlist('image')

            for image in images:
                img  = ProductImage.objects.create(
                        vendor      = Vendor.objects.filter(user=request.user).first(),
                        main        = main,
                        product     = product,
                        image       = image,
                        description = request.POST.get("title")
                    )
                main = False

            return redirect('/product/list/')
        except e:
            print(e);
            return redirect('/product/list/')

    return render(request,'product/hygenic_product.htm', {'form' : form, 'img_form' : img_form})


@login_required
def listProduct(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        productQuery = Product.objects.filter(vendor=Vendor.objects.filter(user=request.user).first())
        # products  = []
        vendor = Vendor.objects.filter(user=request.user).first()
        images = ProductImage.objects.filter(vendor=vendor, main= True)


        # for product in productQuery :
        #     product.img = ProductImage.objects.filter(product=product)
        #     products.append(product)

            # print(product)
            # product['image'] = ProductImage.objects.filter(product=product)
        print(images)

        return render(request,'product/list.htm',{'context': context, 'images' : images})
    except:

        return redirect('/vendor/dashboard/')

@login_required
def detailProduct(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }
        print(id)
        product = Product.objects.get(id=id)
        product_img = ProductImage.objects.filter(product=product)

        return render(request,'product/detail.htm', {'context' : context,'product': product, 'product_img' : product_img})
    except e:
        print(e)
        return redirect('/vendor/dashboard/')
    
def hygenic(request):
    return render(request,'product/hygenic.htm')
def medicine(request):
    return render(request, 'product/medicine.htm')
def device(request):
    return render(request, 'product/device.htm')