from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from myapp.models import Patient,Appointment,Department,Doctor,Prescription,Surgery,Insuarance
from django.http import JsonResponse

def patients_without_insurance(request):
    # Get the current date
    today = timezone.now().date()

    # Calculate the date for one month ago
    one_month_ago = today - timedelta(days=30)

    # app=Appointment.objects.filter(appointment_date__lte=datetime.datetime.today(), 
    #                                appointment_date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
 
    patients = Patient.objects.filter(
        app_p_id__appointment_date__lte=one_month_ago,  # Appointment in the past month
        insuarance_pt__isnull=True  # No insurance (insurance related to patient is null)
    ).distinct()

    # Return as JSON (or you could render a template if needed)
    patient_data = [{"id": patient.id, "name": patient.name} for patient in patients]
    
    # For demonstration, let's return the data as JSON
    return JsonResponse({'patients': patient_data})