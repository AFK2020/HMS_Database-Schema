from django.utils import timezone
from datetime import timedelta, datetime
from myapp.models import (
    Patient,
    Appointment,
    Department,
    Doctor,
    Prescription,
    Surgery,
    Insuarance,
)
from myapp.constants import GenderType, AppointmentStatus,AppointmentType
from django.http import JsonResponse, HttpResponse
from django.db.models import Count, F, Q
from django.db.models.functions import ExtractWeekDay



def patients_without_insurance(request):
    today = timezone.now().date()
    one_month_ago = today - timedelta(days=30)

    patients = Patient.objects.filter(
        app_p_id__appointment_date__gte=one_month_ago,
        app_p_id__appointment_date__lte=today,
        insuarance_pt__isnull=True,  # No insurance (insurance related to patient is null)
    )

    patient_data = [{"id": patient.id, "name": patient.name} for patient in patients]
    return JsonResponse({"patients": patient_data})


def doctors_with_more_appointments(request):
    today = timezone.now().date()
    six_month_ago = today - timedelta(days=30 * 6)
    doctors = Doctor.objects.annotate(count=Count("app_dr_id__id")).filter(
        app_dr_id__appointment_date__gte=six_month_ago,
        app_dr_id__appointment_date__lte=today,
        count__gte=3,
    )

    doctor_data = [
        {
            "id": doctor.id,
            "name": doctor.name,
            # "date": [d.appointment_date for d in doctor.app_dr_id.all()],
        }
        for doctor in doctors
    ]
    return JsonResponse({"doctors": doctor_data})


def update_surgery_status(request):
    today = timezone.now().date()
    Appointment.objects.filter(
        appointment_date__lt=today, status=AppointmentStatus.SCHEDULED.value
    ).update(status=AppointmentStatus.MISSED.value)

    return HttpResponse("Done")


def retrieve_list(request):

    insuarance_providers = Insuarance.objects.filter(patient_id__isnull=False).order_by(
        "provider"
    )

    provider_data = [
        {
            "name": provider.provider,
        }
        for provider in insuarance_providers
    ]
    return JsonResponse({"provider_name": provider_data})


def dept_three_drs(request):

    departments = Department.objects.annotate(count=Count("dr_to_dept")).filter(
        count__gte=3
    )
    dept_data = [
        {"name": dept.name, "doctor": [d.name for d in dept.dr_to_dept.all()]}
        for dept in departments
    ]

    return JsonResponse({"dept_name": dept_data})


def patients_with_prescriptions(request):
    patients = Patient.objects.annotate(
        surgery_count=Count("surgery_patient"), appointment_count=Count("appointments")
    ).filter(surgery_count__gte=1, appointment_count=0)
    print(patients)

    patient_data = [
        {
            "name": p.name,
        }
        for p in patients
    ]
    return JsonResponse({"patient_name": patient_data})


def bulk_create_appointments(requests):
    appointment_list = []
    today = timezone.now().date()

    patients = Patient.objects.filter(
        Q(doctor__name="Meagan Hawkins") & Q(appointments__appointment_date__lte=today)
    )
    patient_data = [
        {
            "name": p.name,
        }
        for p in patients
    ]
    return JsonResponse({"patient_name": patient_data})


def retrieve_prescriptions(request):

    result = (
        Doctor.objects.values("name")
        .annotate(no_of_prescriptions=Count("pres_dr_id"))
        .order_by()
        .filter(no_of_prescriptions__gte=5)
    )
    doctor_data = [
        {"Doctor name": r["name"], "Numeber of Precription": r["no_of_prescriptions"]}
        for r in result
    ]
    return JsonResponse({"patient_name": doctor_data})


def retrieve_app_MassMutual(request):

    patients= Patient.objects.filter(
        insuarance_pt__provider = 'MassMutual'
    ).values_list('name', flat=True)

    appointments = Appointment.objects.filter(
        patient_name__name__in=patients,
        status = AppointmentStatus.SCHEDULED.value
        ).annotate(
            weekday= ExtractWeekDay("appointment_date")
            ).exclude(weekday__in = [7])
    appointment_data = [
        {
        "Patient_name" : a.patient_name.name,
        "Status" : a.status,
        "Priority" : a.type,
        } for a in appointments
    ]
    return JsonResponse({"Appointments" : appointment_data})

def update_priority(request):
    today = timezone.now().date()
    six_months = today - timedelta(days=30*6)
    three_months = today -timedelta(days=30*3)
    
    Appointment.objects.filter(
        appointment_date__lt=six_months,
    ).update(type=AppointmentType.LOW.value)

    Appointment.objects.filter(
        appointment_date__lte=three_months,
        appointment_date__gte=six_months,
    ).update(type=AppointmentType.MEDIUM.value)

    Appointment.objects.filter(
        appointment_date__gt=three_months,
    ).update(type=AppointmentType.HIGH.value)


def retrieve_dr_id(request):

    doctors = Doctor.objects.annotate(surgery_count = Count("surgery_doctor")).filter(
        surgery_count__gte = 3
    )
    doctor_data=[
        {   "Doctor name" : id.name,
            "Doctor id": id.id}
        for id in doctors
        ]
    
    return JsonResponse({"Doctors": doctor_data})


def patients_union(request):
    query1 = Patient.objects.filter(
        app_p_id__isnull = False
    )
    query2 = Patient.objects.filter(
        surgery_patient__isnull = False
    )
    records = (query1 | query2).distinct()
    patient_data=[
        {   "Patient name" : id.name,
            "Patient id": id.id}
        for id in records
        ]
    
    return JsonResponse({"Doctors": patient_data})
        

def doctors_app_pres(request):
    query1_prescription = Doctor.objects.filter(
        pres_dr_id__isnull= False
    )
    query2_appointment = Doctor.objects.filter(
        app_dr_id__isnull = False
    )
    records = (query1_prescription | query2_appointment).distinct()
    doctor_data=[
        {   "Doctor name" : id.name,
            "Doctor id": id.id}
        for id in records
        ]
    return JsonResponse({"Doctors": doctor_data})
        
