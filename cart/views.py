from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required
from django.db import transaction
from django.db.models import Count


from django.shortcuts import redirect, render
# from .forms import MedicineForm
from .models import Cart, CartItem
from product.models import Product,ProductImage
from vendor.models import Vendor
from customer.models import Customer

# Create your views here.
@login_required
def cart(request):
    try:
        context={
            'topic':'Cart',
            'account': 'Home',
            'recent_page': 'cart',
            }

        cart_items = CartItem.objects.filter(cart__customer__user = request.user).order_by('product__vendor')

        return render(request,'cart/cart.htm', {'context' : context, 'cart_items' : cart_items })
    except:
        return render(request,'cart/cart.htm')

@login_required
@transaction.atomic
def addToCart(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

        quantity = 0
        message =""

        if request.method=="POST":

            if(int(request.POST.get('product-quantity'))>0):
                customer = Customer.objects.filter(user=request.user).first()
                cart = Cart.objects.filter(customer=customer)
                product = Product.objects.get(id=id)
                quantity = int(request.POST.get('product-quantity'))

                if cart:
                    cart = Cart.objects.get(customer=customer)
                    cart_update = Cart.objects.filter(customer=customer).update(
                        item_count  = cart.item_count + 1,
                        quantity    = cart.item_count+quantity,
                        total       = cart.total + product.price * quantity,
                        tax         = cart.tax + product.price * quantity * .13,
                        grand_total = cart.grand_total+ product.price * quantity + product.price * quantity * .13
                    )

                    cart_item = CartItem.objects.create(
                        cart = cart,
                        image = ProductImage.objects.filter(main=True, product=product).first(),
                        product = product,
                        unit_price = product.price,
                        quantity = quantity,
                        item_description = product.description
                    )

                else :
                    cart = Cart.objects.create (
                        customer    = customer,
                        item_count  = 1,
                        quantity    = quantity,
                        total       = product.price * quantity,
                        tax         = product.price * quantity * .13 ,
                        grand_total = product.price * quantity + product.price * quantity * .13,
                    )
                
                    cart_item = CartItem.objects.create(
                        cart = cart,
                        image = ProductImage.objects.filter(main=True, product=product).first(),
                        product = product,
                        unit_price = product.price,
                        quantity = quantity,
                        item_description = product.description
                    )

                return redirect('/cart/list/')
                
            else:
                message = "Quantity cannot be zero"


        product = Product.objects.get(id=id)
        product_img = ProductImage.objects.filter(product=product)

        return render(request,'cart/cart-form.htm', {'context' : context,'product': product, 'product_img' : product_img, 'quantity':quantity,'message':message})
    except e:
        print(e)
        return redirect('/product/shop/')

@login_required
@transaction.atomic
def removeFromCart(request,id):
    context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Product',
                }

    message ="The item couldn't be deleted"

    try:
       
        customer = Customer.objects.filter(user=request.user).first()
        cart_item = CartItem.objects.get(id=id)
        cart = Cart.objects.get(customer=customer)

        cart_update = Cart.objects.filter(customer=customer).update(
            item_count  = cart.item_count - 1,
            quantity    = cart.item_count- cart_item.quantity,
            total       = cart.total - cart_item.unit_price * cart_item.quantity,
            tax         = cart.tax - cart_item.unit_price * cart_item.quantity * .13,
            grand_total = cart.grand_total-(cart_item.unit_price * cart_item.quantity + cart_item.unit_price * cart_item.quantity * .13)
        )

        cart_item = CartItem.objects.filter(id=id).delete()       
                
        message = "The item was successfully removed from cart"

        return redirect('/cart/list/')
    except:
        return redirect('/product/shop/')
    

