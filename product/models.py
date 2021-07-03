from django.db import models
from vendor.models import Vendor

# Create your models here.
class Product(models.Model):
    MEDICINE = 'medicine'
    DEVICES = 'devices'
    HYGIENE = 'hygienic_product'

    PRODUCT_TYPES = [
        (MEDICINE, 'Medicine'),
        (DEVICES, 'Devices'),
        (HYGIENE, 'Hygienic Product'),
    ]

    vendor_id = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    meta_title = models.CharField(max_length=120)
    medical_name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    price = models.FloatField()
    quantity = models.IntegerField()
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default=MEDICINE)
    description = models.TextField(max_length=254)
    manufacturer = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)