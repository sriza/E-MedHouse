from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Doctor, User, DoctorImage

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


class doctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('full_name', 'user_name', 'address' , 'email', 'description', 'available_date', 'specialist', 'gender', 'nmc_number', 'charge', 'contact_number', 'degree')

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
    available_date   = forms.DateField(label='Available Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter your available date'}))
    specialist        = forms.CharField(label='Specialist On', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your specialized on'}))
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

class DoctorImageForm(forms.ModelForm):
    class Meta:
        model = DoctorImage
        fields = ('image',)
    image = forms.ImageField(required=False)