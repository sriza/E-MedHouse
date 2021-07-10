from django.shortcuts import render

from .models import Order, OrderItem
from customer.models import Customer
from product.models import Product

# Create your views here.
def checkout(request):
    # form     = MedicineForm(request.POST or None)
    # img_form = ProductImageForm(request.POST or None, request.FILES or None)

    # if form.is_valid():
    #     try : 
    #         main    = True
    #         product = form.save(commit=False)
    #         product.vendor = Vendor.objects.filter(user=request.user).first()
    #         product.product_type = request.POST.get('product_type')
    #         product.save()

    #         images = request.FILES.getlist('image')

    #         for image in images:
    #             img  = ProductImage.objects.create(
    #                     vendor      = Vendor.objects.filter(user=request.user).first(),
    #                     main        = main,
    #                     product     = product,
    #                     image       = image,
    #                     description = request.POST.get("title")
    #                 )
    #             main = False
    #         return redirect('/product/list/')
    #     except:
    #         return redirect('/product/list/')￼

    return render(request,'order/checkout.htm')
