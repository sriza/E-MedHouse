from django.db import models

# Create your models here.
class Vendor(models.Model):
    full_name = models.CharField(max_length=120)
    shop_name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10, default="none")
    dob = models.DateField()
    contact_number = models.IntegerField()
    pan_number = models.CharField(max_length=10)
    vat_number = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)

class VendorImage(models.Model):
    PROFILE = 'profile'
    PAN = 'pan'
    VAT = 'vat'
    CITIZENSHIP = 'citizenship'
    LICENSE = 'license'

    IMAGE_TYPES = [
        (PROFILE, 'Profile Picture'),
        (PAN, 'PAN Card'),
        (VAT, 'VAT'),
        (CITIZENSHIP, 'Citizenship Card'),
        (LICENSE, 'License'),
    ]

    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image_path = models.CharField(max_length=256)
    img_type = models.CharField(max_length=12, choices=IMAGE_TYPES, default=LICENSE)
    timestamp = models.DateTimeField(auto_now_add=True)
