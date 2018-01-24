from django import forms
from django.forms import inlineformset_factory
from .models import Diagnosis, LabTest
from patients.models import Patient

class DiagnosisModelForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        exclude = (
            'patient',
            'timestamp',
            'doctor',
        )
        

class LabTestModelForm(forms.ModelForm):
    class Meta:
        model = LabTest
        exclude = (
            'diagnosis',
            'result',
        )

LabTestFormSet = inlineformset_factory(Patient, LabTest,
                                       form=LabTestModelForm, can_delete=True, min_num=1, extra=1)