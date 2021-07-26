from doctor.views import appointment
from customer.models import Customer
from django.db import models
from django.db.models.deletion import CASCADE
from lab.models import Lab
from vendor.models import User

# Create your models here.
class Service(models.Model):
    CLINICAL_MICROBIOLOGY = 'clinical microbiology'
    CLINICAL_CHEMISTRY = 'clinical chemistry'
    HEMATOLOGY = 'hematology'
    BLOOD_BANK = 'blood bank'
    MOLECULAR_DIAGNOTICS = 'molecular diagnotics'
    REPRODUCTIVE_BIOLOGY = 'reproductive biology'

    SERVICES_TYPES = [
        (CLINICAL_MICROBIOLOGY, 'clinical microbiology'),
        (CLINICAL_CHEMISTRY, 'clinical chemistry'),
        (HEMATOLOGY, 'hematology'),
        (BLOOD_BANK, 'blood bank'),
        (MOLECULAR_DIAGNOTICS, 'molecular diagnotics'),
        (REPRODUCTIVE_BIOLOGY, 'reproductive biology'),
    ]
    
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    meta_title = models.CharField(max_length=120,null=True)
    slug = models.SlugField()
    price = models.FloatField()
    appointment_date = models.CharField(max_length=50,null=True)
    duration = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    expiry_date = models.DateField(null=True)
    packed_date = models.DateField(null=True)
    blood_type = models.CharField(max_length=256)
    service_type = models.CharField(max_length=100, choices=SERVICES_TYPES, default=CLINICAL_MICROBIOLOGY)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    BOOKED   = 'booked'
    FIXED    = 'fixed'
    COMPLETED= 'completed'

    STATUS = [
                (BOOKED, 'Booked'),
                (FIXED, 'Fixed'),
                (COMPLETED, 'Completed'),
            ]


    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    lab_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254)
    price = models.FloatField(null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, default="none")
    contact = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    service= models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default=BOOKED)
    test_title = models.CharField(max_length=30)
    appointment = models.DateTimeField(null=True)
    has_file = models.BooleanField(default=False)

def get_upload_path(instance, filename):
    return 'labappointment/{0}/{1}'.format(instance.appointment.id, filename)    

class LabAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    file = models.FileField(upload_to= get_upload_path ,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)    