from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Customer, User, CustomerImage

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


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'user_name', 'address' ,'email', 'gender', 'contact_number')

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
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
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
          if Customer.objects.filter(user_name=data).count() > 0:
              raise forms.ValidationError("We have a user with this user name. Please try another user name")
          return data

class CustomerImageForm(forms.ModelForm):
    class Meta:
        model = CustomerImage
        fields = ('image',)
    image = forms.ImageField(required=False)

class AppointmentForm(forms.Form):
    class Meta:
        model = Customer
