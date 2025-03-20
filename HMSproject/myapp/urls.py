from django.urls import path
from myapp.views import patients_without_insurance

urlpatterns = [
    path('patients/without-insurance/', patients_without_insurance, name='patients_without_insurance'),
]