from django import forms
from .models import Product, ProductImage

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'meta_title', 'medical_name', 'manufacture_date', 'expiry_date', 'price', 'quantity', 'description','manufacturer')

    MEDICINE = 'medicine'
    DEVICES = 'devices'
    HYGIENE = 'hygienic_product'

    PRODUCT_TYPES = [
        (MEDICINE, 'Medicine'),
        (DEVICES, 'Devices'),
        (HYGIENE, 'Hygienic Product'),
    ]

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the product'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title for the product'}))
    medical_name     = forms.CharField(label='Generic Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the generic name of medicine'}))
    manufacture_date = forms.DateField(label='Manufacture Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the date of manufacture'}))
    expiry_date      = forms.DateField(label='Expiry Date',  widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter expiry date'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
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

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'meta_title', 'price', 'quantity', 'description','manufacturer')

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the product'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title for the product'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
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

class HygenicProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'meta_title', 'manufacture_date', 'expiry_date', 'price', 'quantity', 'description','manufacturer')

    title            = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the name of the product'}))
    meta_title       = forms.CharField(label='Meta Title', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the meta title for the product'}))
    manufacture_date = forms.DateField(label='Manufacture Date', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter the date of manufacture'}))
    expiry_date      = forms.DateField(label='Expiry Date',  widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter expiry date'}))
    price            = forms.FloatField(label='Price', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the price'}))
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


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
