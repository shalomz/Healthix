from django.db import models
from insurance_companies.models import InsuranceCompany


def patient_directory_path(instance, filename):
    # image will be uploaded to MEDIA_ROOT/patient_<patient_code>/profile/<filename>
    return 'patient_{0}/profile/{1}'.format(instance.patient_code, filename)


class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    patient_code = models.CharField(max_length=40)
    mobile_number = models.PositiveIntegerField()
    email = models.EmailField(blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    insurance_company = models.ForeignKey(
        InsuranceCompany, blank=True, null=True, on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=50, blank=True, null=True, unique=True)
    photo = models.ImageField(blank=True, null=True, upload_to=patient_directory_path)

    def __str__(self):
        # Some hacky way of formatting the way the names are displayed
        if self.last_name:
            return self.last_name + ', ' + self.first_name + ' ' + self.middle_name
        else:
            return self.first_name + ' ' + self.middle_name
