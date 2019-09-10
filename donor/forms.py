from django import forms
from django.forms import ModelForm
from .models import Donor

class DonorForm(ModelForm):
    required_css_class = 'required'
    class Meta:
    	# the model this form should be based on
        model = Donor
        # form should include all fields
        fields = '__all__'