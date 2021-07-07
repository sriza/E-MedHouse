from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2
      
    ROLE_CHOICES = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer')
    )
    
    first_name = None
    last_name = None
    username = None
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=254, unique= True, )
    password = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    shop_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    business_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10, default="none")
    dob = models.DateField()
    contact_number = models.IntegerField()
    pan_number = models.CharField(max_length=10)
    vat_number = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

def get_upload_path(instance, filename):
    return 'vendor/{0}/{1}'.format(instance.vendor.id, filename)

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

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to= get_upload_path ,blank=True)
    img_type = models.CharField(max_length=12, choices=IMAGE_TYPES, default=LICENSE)
    timestamp = models.DateTimeField(auto_now_add=True)

    
