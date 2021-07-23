from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Order, OrderItem
from customer.models import Customer
from product.models import Product
from cart.models import Cart, CartItem
from vendor.models import Vendor
from .forms import OrderForm

# Create your views here.
@login_required
@transaction.atomic
def checkout(request,id):
    cart_items = CartItem.objects.filter(cart__customer__user = request.user, product__vendor=id).order_by('product__vendor')
    total = 0
    count = 0

    for item in cart_items:
        total += item.quantity*item.unit_price
        count += item.quantity

    form = OrderForm(request.POST or None)

    if form.is_valid() :
        try :
            vendor = Vendor.objects.get(id=id)
            order = form.save(commit=False)
            order.customer = Customer.objects.filter(user=request.user).first()
            order.status   = 'new'
            order.total    = total
            order.grand_total = total
            order.vendor = vendor
            order.items = count 
            order.save()


            for item in cart_items:
                cart_item = OrderItem.objects.create(
                        order = order,
                        image = item.image,
                        product = item.product,
                        unit_price = item.unit_price,
                        quantity = item.quantity,
                    )
                
                removeFromCart(Customer.objects.filter(user=request.user).first(),item.id)
    
            return redirect('/order/payment/{0}'.format(order.id))
    
        except e:
            return render(request,'customer/index.htm')    

    return render(request,'order/checkout.htm', {'items': cart_items, 'total': total, 'form' : form, 'id': id} )

@login_required
@transaction.atomic
def removeFromCart(customer, id):
    cart_item = CartItem.objects.get(id=id)
    cart = Cart.objects.get(customer=customer)

    cart_update = Cart.objects.filter(customer=customer).update(
        item_count  = cart.item_count - 1,
        quantity    = cart.item_count- cart_item.quantity,
        total       = cart.total - cart_item.unit_price * cart_item.quantity,
        tax         = cart.tax - cart_item.unit_price * cart_item.quantity * .13,
        grand_total = cart.grand_total-(cart_item.unit_price * cart_item.quantity + cart_item.unit_price * cart_item.quantity * .13)
    )

    CartItem.objects.filter(id=id).delete() 

@login_required
@transaction.atomic
def payment(request,id):
    order_items = OrderItem.objects.filter(order__customer__user = request.user, order__id=id).order_by('product__vendor')

    total = 0
    order_id = 0

    for item in order_items:
        total += item.quantity*item.unit_price

    return render(request,'order/payment.htm', {'items': order_items, 'total': total, 'id':id} )

@login_required
@transaction.atomic
def paymentMade(request,id):
    try:
        Order.objects.filter(id=id).update(
            payment=True
        )
        
        return render(request,'medicalapp/confirmation.htm' )
    except:
        return redirect('/order/payment/'.id)

@login_required
@transaction.atomic
def cancelOrder(request,id) :
    try :
        Order.objects.filter(id=id).delete()

        return redirect('/customer/order')
    except:
        return render(request,'customer/index.htm')  

@login_required
@transaction.atomic
def statusProcessing(request,id):
    try:
        Order.objects.filter(id=id).update(
            status='processing'
        )
        
        return redirect('/vendor/order')
    except:
        return redirect('/vendor/order')

@login_required
@transaction.atomic
def statusCompleted(request,id):
    try:
        Order.objects.filter(id=id).update(
            status='completed'
        )
        
        return redirect('/vendor/order')
    except:
        return redirect('/vendor/order')


      
                