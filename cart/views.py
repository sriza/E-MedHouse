from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required
from django.db import transaction

from django.shortcuts import redirect, render
# from .forms import MedicineForm
from .models import Cart, CartItem
from vendor.models import Vendor

# Create your views here.
def cart(request):
    return render(request,'cart/cart.htm')

@login_required
@transaction.atomic
def addToCart(request):
    # form     = MedicineForm(request.POST or None)
    # img_form = ProductImageForm(request.POST or None, request.FILES or None)

    # if form.is_valid():
    try : 
        # main    = True
        # product = form.save(commit=False)
        # product.vendor = Vendor.objects.filter(user=request.user).first()
        # product.product_type = request.POST.get('product_type')
        # product.save()

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

    # return render(request,'product/medicine.htm', {'form' : form, 'img_form' : img_form})
