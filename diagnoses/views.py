from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from .forms import DiagnosisModelForm, LabTestFormSet
from .models import Diagnosis, LabTest, LabResult
from patients.models import Patient
# Create your views here.

def diagnose(request, patient_code):
    patient = get_object_or_404(Patient, patient_code = patient_code)    
    if request.method == 'POST':
        diagnosis_form = DiagnosisModelForm(request.POST or None)
        lab_form_set = LabTestFormSet(request.POST, instance=patient)
        if diagnosis_form.is_valid() and lab_form_set.is_valid():
            diagnosis = diagnosis_form.save(commit=False)
            diagnosis.patient = patient
            diagnosis.doctor = request.user
            diagnosis.possible_diagnosis = request.POST.get('possible_diagnosis')
            diagnosis.save()

            new_lab, new_history = [], []
            
            for lab_form in lab_form_set:

                specimen = lab_form.cleaned_data.get(
                    'specimen')
                period = lab_form.cleaned_data.get(
                    'period')
                test = lab_form.cleaned_data.get(
                    'test')
                    
                if specimen and test and period:
                    new_history.append(LabTest(patient=patient, specimen=specimen,
                                               period=period, test=test))

            try:
                with transaction.atomic():
                    LabTest.objects.filter(patient=patient).delete()
                    LabTest.objects.bulk_create(new_lab)
                    messages.success(request, 'Success')
            except IntegrityError:
                messages.error(request, 'Error')
                return redirect('/diagnose/'+patient_code)
    else:
        diagnosis_form = DiagnosisModelForm()
        lab_form_set = LabTestFormSet(instance=patient)
    return render(request, 'doctor_diagnosis.html', {'diagnosis_form': diagnosis_form, 'patient': patient, 'lab_form_set': lab_form_set})


def results(request, patient_code):
    patient = get_object_or_404(Patient, patient_code=patient_code)
    tests = LabTest.objects.filter(patient=patient)
    results = LabResult.objects.filter(lab_test__patient=patient)
    print(results)
    return render(request, 'results.html', {'tests': tests, 'results': results})


def diagnosis_histories(request, patient_code):
    patient = get_object_or_404(Patient, patient_code=patient_code)
    histories = Diagnosis.objects.filter(patient=patient)
    return render(request, 'diagnosis_history.html', {'histories': histories})