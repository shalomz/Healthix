from django.conf.urls import url
from .views import new_patient, all_patients, patient_api
urlpatterns = [
    url(r'^register/$', new_patient, name='register_patient'),
    url(r'^patients/$', all_patients, name='all_patients'),
    url(r'^patient-api/$', patient_api, name='patients_api'),
]