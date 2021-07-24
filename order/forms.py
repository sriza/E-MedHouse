from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'shipping_location', 'map_url', 'contact_number', 'email')

    full_name         = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the full name'}))
    shipping_location = forms.CharField(label='Shiping location', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the shipping location'}))
    map_url           = forms.CharField(label='Map Url', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the google map url of shipping location'}))
    contact_number    = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    email             = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))

    
    # def clean_expiry_date(self):
    #     manufacture_date = self.cleaned_data.get("manufacture_date")
    #     expiry_date = self.cleaned_data.get("expiry_date")
    #     if manufacture_date and expiry_date and expiry_date < manufacture_date:
    #         raise forms.ValidationError("Expiry date can't be before manufacture date.")
    #     return expiry_date
