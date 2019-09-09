from django import forms
from django.forms import ModelForm
from .models import Donor

class DonorForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Donor
        fields = '__all__'