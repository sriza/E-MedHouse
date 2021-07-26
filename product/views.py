from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator

from django.shortcuts import redirect, render
from .forms import MedicineForm, DeviceForm, HygenicProductForm , ProductImageForm, ProductImageEditForm
from .models import Product, ProductImage
from vendor.models import Vendor
from customer.models import Review

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
    object   = Product.objects.get(id=id) 
    img      = ProductImage.objects.filter(product=object)
    form     = MedicineForm(instance=object, data=request.POST or None)
    img_form = ProductImageEditForm(request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product = form.save()

            images = request.FILES.getlist('image')

            if bool(images):
                ProductImage.objects.filter(product=product).delete()

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
            print(e)
            return redirect('/product/list/')

    return render(request,'product/updatemedicine.htm', {'form' : form, 'img_form' : img_form, 'images' : img,  'product':object})

@login_required
@transaction.atomic
def updateDevice(request,id):
    object   = Product.objects.get(id=id) 
    form     = DeviceForm(instance=object,data=request.POST or None)
    img      = ProductImage.objects.filter(product=object)
    img_form = ProductImageEditForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product = form.save()

            images = request.FILES.getlist('image')
            
            if bool(images):
                ProductImage.objects.filter(product=product).delete()

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

    return render(request,'product/updatedevice.htm', {'form' : form, 'img_form' : img_form, 'images' : img, 'product':object})

@login_required
@transaction.atomic
def updateHygenicProduct(request,id):
    object   = Product.objects.get(id=id) 
    img      = ProductImage.objects.filter(product=object)
    form     = HygenicProductForm(instance = object, data=request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            main    = True
            product=form.save()
          
            images = request.FILES.getlist('image')
            
            if bool(images):
                ProductImage.objects.filter(product=product).delete()

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

    return render(request,'product/updatehygenic_product.htm', {'form' : form, 'img_form' : img_form, 'images' : img, 'product':object})

@login_required
def listProduct(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        vendor = Vendor.objects.filter(user=request.user).first()

        if request.method == "POST" :
            title = request.POST.get('title')
          
            if title:
                images_list = ProductImage.objects.filter((Q(product__title__contains = title)| Q(product__meta_title__contains = title)| Q(product__medical_name__contains = title)| Q(product__description__contains = title)) & Q(main=True) & Q(vendor=vendor)).order_by('product__expiry_date')
            else :
                images_list = ProductImage.objects.filter(main= True,vendor=vendor)

        else :
            images_list = ProductImage.objects.filter(main= True, vendor=vendor)

        paginator = Paginator(images_list, 10)

        page_number = request.GET.get('page')
        images = paginator.get_page(page_number)

        return render(request,'product/list.htm',{'context': context, 'images' : images})
    except e:

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
        category = ''
        title = ''

        if request.method == "POST" :
            print(request.POST)
            category = request.POST.get('product_type')
            title = request.POST.get('title')
            category_arr = {
                'Medicine' : 'medicine',
                'Hygenic Product' : 'hygenic_product',
                'Device'      : 'device'
            }
            
            if category!='Search by category' and title=='':
                images_list = ProductImage.objects.filter(product__product_type__exact = category_arr[category], main=True).order_by('product__expiry_date')
            elif title and category=="Search by category":
                images_list = ProductImage.objects.filter((Q(product__title__contains = title)| Q(product__meta_title__contains = title)| Q(product__medical_name__contains = title)| Q(product__description__contains = title)) & Q(main=True) ).order_by('product__expiry_date')
            elif category!="Search by category" and title :
                images_list = ProductImage.objects.filter((Q(product__product_type__exact = category_arr[category])| Q(product__title__contains = title)| Q(product__meta_title__contains = title)| Q(product__medical_name__contains = title)| Q(product__description__contains = title)) & Q(main=True) ).order_by('product__expiry_date')
            else :
                images_list = ProductImage.objects.filter(main= True)
            
            if category=='Search by category':
                category =''

        else :
            images_list = ProductImage.objects.filter(main= True)
        
        paginator = Paginator(images_list, 9)

        page_number = request.GET.get('page')
        images = paginator.get_page(page_number)

        return render(request,'product/shop.htm',{'context': context, 'images' : images, 'category' : category, 'title' : title })
    except e:
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
        reviews = Review.objects.filter(product=product)

        return render(request,'product/customer_detail.htm', {'context' : context,'product': product, 'product_img' : product_img, 'reviews' : reviews})
    except e:
        print(e)
        return redirect('/customer/dashboard/')

@login_required  
def deleteProduct(request,id):
    try : 
        Product.objects.filter(id=id).delete()

        return redirect('/product/list/')
    except:
        return redirect('/vendor/dashboard/')