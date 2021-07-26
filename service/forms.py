from django import forms
from django.db.models import fields
from .models import Service,Appointment, LabAppointment


class MicrobiologyForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment_date', 'duration', 'price', 'description')

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

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title of the service'}))
    appointment_date = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration

class ChemistryForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment_date', 'duration', 'price', 'description')

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

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title of the service'}))
    appointment_date = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration

class HematologyForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment_date', 'duration', 'price', 'description')

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
    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title of the service'}))
    appointment_date = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration  

class BloodBankForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'packed_date', 'expiry_date', 'blood_type', 'price', 'description')

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

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    packed_date      = forms.DateField(label='Packed Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the available appointment time'}))
    expiry_date      = forms.DateField(label='Expiry Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the available appointment time'}))
    blood_type       = forms.CharField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    quantity         = forms.IntegerField(label='Quantity', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the quantity'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    

    def clean_expiry_date(self):
        packed_date = self.cleaned_data.get("packed_date")
        expiry_date = self.cleaned_data.get("expiry_date")
        if packed_date and expiry_date and expiry_date < packed_date:
            raise forms.ValidationError("Expiry date can't be before manufacture date.")
        return expiry_date

class MolecularDiagnoticsForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment_date', 'duration', 'price', 'description')

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

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title of the service'}))
    appointment_date = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("Products can't have quantity less than one.")
        return duration
    
    
class ReproductiveBiologyForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment_date', 'duration', 'price', 'description')

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

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the service/test type'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title of the service'}))
    appointment_date = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration
    
                         
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('full_name', 'email', 'gender', 'address', 'dob', 'contact_number', 'appointment')

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_TYPES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

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

    full_name        = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name','disabled': True}))
    email            = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email','disabled': True}))
    address          = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address','disabled': True}))
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender','disabled': True}))
    dob              = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter your date of birth','disabled': True}))
    contact_number          = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number','disabled': True}))
    appointment      = forms.DateTimeField(label='Date Appointment',widget=forms.TextInput(attrs={'class':'form-control form_datetime' ,'placeholder': 'Enter your appointment hour'}))

class LabReportForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('full_name', 'email', 'gender', 'address', 'dob', 'contact', 'appointment')

    full_name        = forms.CharField(label='Full Name',required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name', 'disabled': True}))
    email            = forms.EmailField(label='Email',required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email', 'disabled': True}))
    address          = forms.CharField(label='Address', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address', 'disabled': True}))
    dob              = forms.DateField(label='Date Of Birth',required=False, widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter your date of birth', 'disabled': True}))
    contact          = forms.IntegerField(label='Contact Number',required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number', 'disabled': True}))
    appointment      = forms.DateTimeField(label='Date Appointment',required=False, widget=forms.TextInput(attrs={'class':'form-control form_datetime' ,'placeholder': 'Enter your appointment hour', 'disabled': True}))
    
    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = LabAppointment
        fields = ('file',)
    file = forms.FileField()