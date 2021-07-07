from django.db import models
from vendor.models import User

# Create your models here.
def get_upload_path(instance, filename):
    return 'customer/{0}/{1}'.format(instance.customer.id, filename)
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="none")
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    contact_number = models.IntegerField()
    address = models.CharField(max_length=200, null=True)

class CustomerImage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to= get_upload_path ,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
