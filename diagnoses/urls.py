from django.conf.urls import url
from .views import diagnose, results, diagnosis_histories

urlpatterns = [
    url(r'^diagnosis/(?P<patient_code>[-\w]+)/$', diagnose, name='diagnose'),
    url(r'^results/(?P<patient_code>[-\w]+)/$', results, name = 'results'),
    url(r'^diagnoses/(?P<patient_code>[-\w]+)/$', diagnosis_histories, name='diagnosis_histories'),
]
