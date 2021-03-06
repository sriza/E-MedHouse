from vendor.models import Vendor
from django.db import models
from customer.models import Customer
from product.models import Product, ProductImage

# Create your models here.
class Order(models.Model):
    NEW         = 'new'
    CANCELLED   = 'cancelled'
    PROCESSING  = 'processing'
    COMPLETED   = 'completed'

    STATUS = [
        (NEW, 'New'),
        (CANCELLED, 'Cancelled'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed'),
    ]

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    total = models.FloatField()
    items = models.IntegerField()
    payment = models.BooleanField(default=False)
    shipping_cost = models.FloatField(null=True)
    grand_total = models.FloatField()
    shipping_location = models.CharField(max_length=120)
    full_name = models.CharField(max_length=256)
    map_url = models.CharField(max_length=256, null= True)
    contact_number = models.IntegerField()
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS, default=NEW)
    timestamp = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)