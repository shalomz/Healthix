import datetime

from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Sum
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string


from .forms import PatientRegisterForm
from .models import Patient
from insurance_companies.models import InsuranceCompany

def new_patient(request):
    companies = InsuranceCompany.objects.all()
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            new_patient = form.save(commit=False)
            p = Patient.objects.last()
            if not p:
                new_patient.patient_code = 'HEALTHIX-{}-001'.format(
                    datetime.datetime.now().year)
            else:
                if p.id < 10:

                    new_patient.patient_code = 'HEALTHIX-{}-00{}'.format(
                        datetime.datetime.now().year, str(p.id + 1))
                elif p.id >= 10 and p.id < 100:
                    new_patient.patient_code = 'HEALTHIX-{}-0{}'.format(
                        datetime.datetime.now().year, str(p.id + 1))
                else:
                    new_patient.patient_code = 'HEALTHIX-{}-{}'.format(
                        datetime.datetime.now().year, str(p.id + 1))
            company = request.POST['insurances']
            print(company)
            number = request.POST.get('insurance_number')
            print(number)
            ins_comp = InsuranceCompany.objects.get(name=company)
            new_patient.insurance_company = ins_comp
            new_patient.insurance_number = number
            new_patient.save()
            return redirect('/')
    else:
        form = PatientRegisterForm()
    return render(request, 'new_patient.html', {'form': form, 'companies': companies})


def all_patients(request):
    patients = Patient.objects.all()
    return render(request, 'all_patients.html', {'patients': patients})


def patient_api(request):
    patients = Patient.objects.all()
    json = serializers.serialize(
        'json', patients, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json, content_type='application/json')
