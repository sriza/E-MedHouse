from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction

from django.shortcuts import get_object_or_404, redirect, render
from .forms import MedicineForm, DeviceForm, HygenicProductForm , ProductImageForm
from .models import Product, ProductImage
from vendor.models import Vendor

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
        except:
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
        except:

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
        except :
            return redirect('/product/list/')

    return render(request,'product/hygenic_product.htm', {'form' : form, 'img_form' : img_form})

@login_required
@transaction.atomic
def updateMedicine(request,id):
    print(id)
    object   = Product.objects.get(id=id) 
    form     = MedicineForm(instance=object, data=request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            # main    = True
            form.save()

            images = request.FILES.getlist('image')

            # for image in images:
            #     img  = ProductImage.objects.create(
            #             vendor      = Vendor.objects.filter(user=request.user).first(),
            #             main        = main,
            #             product     = product,
            #             image       = image,
            #             description = request.POST.get("title")
            #         )
            #     main = False
            return redirect('/product/list/')
        except:
            return redirect('/product/list/')

    return render(request,'product/updatemedicine.htm', {'form' : form, 'product':object})

@login_required
@transaction.atomic
def updateDevice(request,id):
    object   = Product.objects.get(id=id) 
    form     = DeviceForm(instance=object,data=request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()

            # images = request.FILES.getlist('image')

            # for image in images:
            #     img  = ProductImage.objects.create(
            #             vendor      = Vendor.objects.filter(user=request.user).first(),
            #             main        = main,
            #             product     = product,
            #             image       = image,
            #             description = request.POST.get("title")
            #         )
            #     main = False

            return redirect('/product/list/')
        except:

            return redirect('/product/list/')

    return render(request,'product/updatedevice.htm', {'form' : form, 'product':object})

@login_required
@transaction.atomic
def updateHygenicProduct(request,id):
    object   = Product.objects.get(id=id) 
    form     = HygenicProductForm(instance = object, data=request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
          
            images = request.FILES.getlist('image')

            # for image in images:
            #     img  = ProductImage.objects.create(
            #             vendor      = Vendor.objects.filter(user=request.user).first(),
            #             main        = main,
            #             product     = product,
            #             image       = image,
            #             description = request.POST.get("title")
            #         )
            #     main = False

            return redirect('/product/list/')
        except :
            return redirect('/product/list/')

    return render(request,'product/updatehygenic_product.htm', {'form' : form, 'product':object})

@login_required
def listProduct(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        vendor = Vendor.objects.filter(user=request.user).first()
        images = ProductImage.objects.filter(vendor=vendor, main= True)

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

        product = Product.objects.get(id=id)
        product_img = ProductImage.objects.filter(product=product)

        return render(request,'product/detail.htm', {'context' : context,'product': product, 'product_img' : product_img})
    except:

        return redirect('/vendor/dashboard/')

@login_required
def shopProduct(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Shop',
                }

        if request.method == "POST" :
            print(request.POST)
            category = request.POST.get('product_type')
            title = request.POST.get('title')
            
            # images = ProductImage.objects.filter(Q(product__product_type__exact = category)| 
            #                                      Q(product__title__contains = title)|
            #                                      Q(product__meta_title__contains = title)|
            #                                      Q(product__medical_name__contains = title)|
            #                                      Q(product__description__contains = title)
            #                                      ).order_by('product__expiry_date')
            # images = ProductImage.objects.filter(main= True,product__product_type = category)
            images = ProductImage.objects.filter(main= True)

        else :
            images = ProductImage.objects.filter(main= True)

        return render(request,'product/shop.htm',{'context': context, 'images' : images})
    except:
        return redirect('/customer/dashboard/')

@login_required
def shopProductDetail(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Product Detail',
                }

        product = Product.objects.get(id=id)
        product_img = ProductImage.objects.filter(product=product)

        return render(request,'product/customer_detail.htm', {'context' : context,'product': product, 'product_img' : product_img})
    except:
        return redirect('/vendor/dashboard/')

@login_required  
def deleteProduct(request,id):
    try : 
        Product.objects.filter(id=id).delete()

        return redirect('/product/list/')
    except:
        return redirect('/vendor/dashboard/')