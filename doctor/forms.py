from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Doctor, DoctorAppointment, User, DoctorImage
from django.utils import timezone

user = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter your password'}))

    def clean(self):
        data = self.cleaned_data
        email  = data.get("email")
        password  = data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            raise forms.ValidationError("Invalid credentials")

        return data


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('full_name', 'user_name', 'address' , 'email', 'description', 'available_day', 'specialist', 'gender', 'nmc_number', 'charge', 'contact_number', 'degree')

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_TYPES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    full_name        = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name'}))
    user_name        = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your user name'}))
    address          = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address'}))
    email            = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about yourself'}))
    available_day    = forms.CharField(label='Available Day', widget=forms.Textarea(attrs={'class':'form-control' ,'placeholder': 'Enter your available days separated by commas'}))
    specialist       = forms.CharField(label='Specialist On', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your specialized on'}))
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender'}))
    nmc_number       = forms.CharField(label='NMC Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your NMC Number'}))
    charge           = forms.FloatField(label='Charge', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your charge fee'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    degree           = forms.CharField(label='Degree',widget=forms.TextInput({'class':'form-control','placeholder':'Enter your degree'}))
    password         = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
    
    def clean_email(self):
          data = self.cleaned_data['email']
          if User.objects.filter(email=data).count() > 0:
              raise forms.ValidationError("We have a user with this user email-id")
          return data

    def clean_user_name(self):
          data = self.cleaned_data['user_name']
          if Doctor.objects.filter(user_name=data).count() > 0:
              raise forms.ValidationError("We have a user with this user name. Please try another user name")
          return data

class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('full_name', 'user_name', 'address', 'description', 'available_day', 'specialist', 'gender', 'charge', 'contact_number', 'degree')

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_TYPES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    full_name        = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name'}))
    user_name        = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your user name'}))
    address          = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about yourself'}))
    available_day    = forms.CharField(label='Available Day', widget=forms.Textarea(attrs={'class':'form-control' ,'placeholder': 'Enter your available days separated by commas'}))
    specialist       = forms.CharField(label='Specialist On', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your specialized on'}))
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender'}))
    charge           = forms.FloatField(label='Charge', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your charge fee'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    degree           = forms.CharField(label='Degree',widget=forms.TextInput({'class':'form-control','placeholder':'Enter your degree'}))

class DoctorImageForm(forms.ModelForm):
    class Meta:
        model = DoctorImage
        fields = ('image',)
    image = forms.ImageField(required=False)

class DoctorImageEditForm(forms.ModelForm):
    class Meta:
        model = DoctorImage
        fields = ('image',)
    image = forms.ImageField(required=False)


class DoctorAppointmentForm(forms.ModelForm):
    class Meta:
        model = DoctorAppointment
        fields = ('patient_name', 'contact_number','address', 'email','description')

    patient_name     = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your user name'}))
    address          = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    email            = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about your health issue'}))

class DoctorAppointmentEditForm(forms.ModelForm):
    class Meta:
        model = DoctorAppointment
        fields = ('patient_name','address','contact_number','email','description','fixed_on',)

    patient_name     = forms.CharField(label='User Name', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your user name', 'disabled': True}))
    address          = forms.CharField(label='Address', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address', 'disabled': True}))
    contact_number   = forms.IntegerField(label='Contact Number', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number', 'disabled': True}))
    email            = forms.EmailField(label='Email', required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email', 'disabled': True}))
    description      = forms.CharField(label='Description',required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about your health issue', 'disabled': True}))
    fixed_on         = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'class':'form-control datetimepicker' ,'placeholder': 'Enter the appointment date'}))

    def clean_fixed_on(self):
            fixed_on = self.cleaned_data.get("fixed_on")
            print(timezone.now() > fixed_on)
            if fixed_on and timezone.now() > fixed_on:
                raise forms.ValidationError("Appointment date can't be set before today.")
            return fixed_on