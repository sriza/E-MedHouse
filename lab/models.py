from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators
from vendor.models import User
# Create your models here.



class Lab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    lab_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    business_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    gender = models.CharField(max_length=10, default="none")
    contact_number = models.IntegerField()
    pan_number = models.CharField(max_length=10)
    vat_number = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    services = models.CharField(validators.validate_comma_separated_integer_list, max_length=200)
    branches = models.IntegerField()
    # branLocation = models.CharField(validators.validate_comma_separated_integer_list, max_length=200)

def get_upload_path(instance, filename):
    return 'lab/{0}/{1}'.format(instance.lab.id, filename)    
class LabImage(models.Model):
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

    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to= get_upload_path ,blank=True)
    img_type = models.CharField(max_length=12, choices=IMAGE_TYPES, default=LICENSE)
    timestamp = models.DateTimeField(auto_now_add=True)
