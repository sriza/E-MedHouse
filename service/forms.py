from django import forms
from .models import Service

class MicrobiologyForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment', 'duration', 'price', 'description')

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
    appointment      = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
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
        fields = ('title', 'meta_title', 'appointment', 'duration', 'price', 'description')

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
    appointment      = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
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
        fields = ('title', 'meta_title', 'appointment', 'duration', 'price', 'description')

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
    appointment      = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
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
    

    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration
    
    def clean_expiry_date(self):
        packed_date = self.cleaned_data.get("packed_date")
        expiry_date = self.cleaned_data.get("expiry_date")
        if packed_date and expiry_date and expiry_date < packed_date:
            raise forms.ValidationError("Expiry date can't be before manufacture date.")
        return expiry_date

class MolecularDiagnoticsForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'meta_title', 'appointment', 'duration', 'price', 'description')

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
    appointment      = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
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
        fields = ('title', 'meta_title', 'appointment', 'duration', 'price', 'description')

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
    appointment      = forms.CharField(label='Appointment Time', widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter the available appointment time'}))
    duration         = forms.IntegerField(label='Result Duration',  widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Enter result duration'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the service'}))
    
    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        if duration < 1 :
            raise forms.ValidationError("duration can't have quantity less than one.")
        return duration
    
                         

