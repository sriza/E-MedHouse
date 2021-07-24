from django.db import models
from vendor.models import User
from customer.models import Customer

# Create your models here.
def get_upload_path(instance, filename):
    return 'doctor/{0}/{1}'.format(instance.doctor.id, filename)
    
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="none")
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    degree = models.CharField(max_length=200)
    available_day = models.CharField(max_length=255)
    specialist = models.CharField(max_length=200)
    charge = models.FloatField()
    contact_number = models.IntegerField()
    nmc_number = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

class DoctorImage(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to= get_upload_path ,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class DoctorAppointment(models.Model):
    BOOKED   = 'booked'
    FIXED    = 'fixed'
    COMPLETED= 'completed'

    STATUS = [
                (BOOKED, 'Booked'),
                (FIXED, 'Fixed'),
                (COMPLETED, 'Completed'),
            ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=120)
    contact_number = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    description = models.TextField(null=True)
    payment = models.BooleanField(default=False)
    appointment_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS, default=BOOKED)
    timestamp = models.DateTimeField(auto_now_add=True)
    fixed_on  = models.DateTimeField(null=True)
