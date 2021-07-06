from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('title', 'meta_title', 'gender', 'dob', 'contact_number', 'pan_number', 'vat_number', 'shop_name', 'business_name')

    MEDICINE = 'medicine'
    DEVICES = 'devices'
    HYGIENE = 'hygienic_product'

    PRODUCT_TYPES = [
        (MEDICINE, 'Medicine'),
        (DEVICES, 'Devices'),
        (HYGIENE, 'Hygienic Product'),
    ]

    full_name        = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name'}))
    email            = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    address            = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address'}))
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender'}))
    dob              = forms.CharField(label='Date Of Birth', widget=forms.TextInput(attrs={'class':'form-control', 'id':'datepicker' ,'placeholder': 'Enter your date of birth'}))
    dob              = forms.CharField(label='Date Of Birth', widget=forms.TextInput(attrs={'class':'form-control', 'id':'datepicker' ,'placeholder': 'Enter your date of birth'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    pan_number       = forms.CharField(label='PAN Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your PAN number'}))
           = forms.CharField(label='VAT Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your VAT number'}))
    description    = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Enter your pharmacy name'}))
    manufacturer   = forms.CharField(label='Product Manufacturer', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your registered business name'}))

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


class RegistrationImageForm(forms.ModelForm):
    class Meta:
        model = VendorImage
        fields = ('image',)
    image = forms.ImageField(required=False)
