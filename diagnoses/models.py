from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User

class Lab(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

class Diagnosis(models.Model):
    VISIT_TYPES = (
        ('Inpatient', 'Inpatient'),
        ('Outpatient', 'Outpatient')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    possible_diagnosis = models.TextField()
    visit_type = models.CharField(max_length=30, choices=VISIT_TYPES)

    def __str__(self):
        return('Diagnosis for {}'.format(self.patient))


class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specimen = models.CharField(max_length=30)
    test = models.CharField(max_length=60)
    period = models.PositiveIntegerField()
    lab = models.ForeignKey(Lab, blank=True, null=True)

    def __str__(self):
        return('Test {}'.format(self.test))

class LabResult(models.Model):
    lab_test = models.ForeignKey(LabTest)
    result = models.TextField()

    def __str__(self):
        return(self.result)

