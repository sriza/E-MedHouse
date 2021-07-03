from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=120)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="none")
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    contact_number = models.IntegerField()
