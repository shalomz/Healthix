from django.contrib import admin
from .models import Diagnosis, LabTest, LabResult
# Register your models here.

admin.site.register(Diagnosis)
admin.site.register(LabTest)
admin.site.register(LabResult)