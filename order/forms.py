from django import forms
from .models import Product, ProductImage

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('shipping_cost')

    full_name         = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the full name'}))
    shipping_location = forms.CharField(label='Shiping location', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the shipping location'}))
    map_url           = forms.CharField(label='Map Url', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the google map url of shipping location'}))
    contact_number    = forms.CharField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the contact number'}))
    email             = forms.EmailField(label='Email',  widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter your email'}))
    price             = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
    shipping_cost     = forms.IntegerField(label='Quantity', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the quantity'}))

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1 :
            raise forms.ValidationError("Products can't have quantity less than one.")
        return quantity
    
    def clean_expiry_date(self):
        manufacture_date = self.cleaned_data.get("manufacture_date")
        expiry_date = self.cleaned_data.get("expiry_date")
        if manufacture_date and expiry_date and expiry_date < manufacture_date:
            raise forms.ValidationError("Expiry date can't be before manufacture date.")
        return expiry_date
