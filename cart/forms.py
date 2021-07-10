from django import forms
from .models import CartItem

class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity', 'description','manufacturer')

    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title for the product'}))
    medical_name     = forms.CharField(label='Generic Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the generic name of medicine'}))
    manufacture_date = forms.DateField(label='Manufacture Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the date of manufacture'}))
    expiry_date      = forms.DateField(label='Expiry Date',  widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter expiry date'}))
    quantity         = forms.IntegerField(label='Quantity', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the quantity'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about the product'}))
    manufacturer     = forms.CharField(label='Product Manufacturer', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the manufacturer'}))

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