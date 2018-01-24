from django import forms 
from .models import Patient


class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = (
            'patient_code',
            'insurance_company',
            'insurance_number'
        )