from django import forms
from .models import NGO, donation_request

class NGO_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ('ngo_name','domain','head_of_ngo','contactNo','email','registration_cerificate_Trust_Society','certificate_12A','beneficiary_profiles')

class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('donation_description','donation_amount')
