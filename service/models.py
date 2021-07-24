from django.db import models
from lab.models import Lab

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
    appointment = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    # quantity = models.IntegerField()
    expiry_date = models.DateField(null=True)
    packed_date = models.DateField(null=True)
    blood_type = models.CharField(max_length=256)
    service_type = models.CharField(max_length=100, choices=SERVICES_TYPES, default=CLINICAL_MICROBIOLOGY)
    description = models.TextField()
    lab_name = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

