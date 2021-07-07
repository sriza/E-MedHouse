from django.db import models
from vendor.models import Vendor
from customer.models import Customer
from product.models import Product

# Create your models here.
class Cart(models.Model):
    # NEW         = 'new'
    # CANCELLED   = 'cancelled'
    # PROCESSING  = 'processing'
    # COMPLETED   = 'completed'

    # STATUS = [
    #     (NEW, 'New'),
    #     (CANCELLED, 'Cancelled'),
    #     (PROCESSING, 'Processing'),
    #     (COMPLETED, 'Completed'),
    # ]
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    item_count = models.IntegerField()
    quantity = models.IntegerField()
    total = models.FloatField()
    tax = models.FloatField()
    grand_total = models.FloatField()
    payment = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=256, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    item_description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)