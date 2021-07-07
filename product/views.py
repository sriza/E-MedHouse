from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required
from django.db import transaction
 

from django.shortcuts import redirect, render
from .forms import ProductForm, ProductImageForm
from .models import Product, ProductImage
from vendor.models import Vendor
# Create your views here.

@login_required
@transaction.atomic
def createProduct(request):
    form     = ProductForm(request.POST or None)
    img_form = ProductImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        try : 
            product = form.save(commit=False)
            product.vendor = Vendor.objects.filter(user=request.user).first()
            product.product_type = request.POST.get('product_type')
            product.save()
            print(request.POST)
            print(request.FILES)

            img             = img_form.save(commit=False)
            img.product     = product
            img.description = request.POST.get("title")
            img.save()

            return redirect('/product/list/')
        except e:
            print(e);
            return redirect('/product/list/')

    return render(request,'product/form.htm', {'form' : form, 'img_form' : img_form})


@login_required
def listProduct(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        productQuery = Product.objects.filter(vendor=Vendor.objects.filter(user=request.user).first())
        products  = []

        for product in productQuery :
            product.img = ProductImage.objects.filter(product=product)
            products.append(product)

            # print(product)
            # product['image'] = ProductImage.objects.filter(product=product)

        return render(request,'product/list.htm',{'context': context, 'products' : products})
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
        product_img = ProductImage.objects.get(product=product)

        return render(request,'product/detail.htm', {'context' : context,'product': product, 'product_img' : product_img})
    except e:
        print(e)
        return redirect('/vendor/dashboard/')
    
