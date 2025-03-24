from django.urls import path
from myapp.views import patients_without_insurance,doctors_with_more_appointments,update_surgery_status
from myapp.views import retrieve_list,dept_three_drs, patients_with_prescriptions,bulk_create_appointments,retrieve_prescriptions
from myapp.views import retrieve_app_MassMutual,patients_doctors,update_priority, retrieve_dr_id,patients_union,fetch_doctors
from myapp.views import doctors_app_pres, doctor_specializations,prescription_pain_killer,doctors_names,patiente_with_insurance
from myapp.views import appointments_thirty_days,oldest_youngest_patients,dept_doctors,cardiology_appointments,difference
from myapp.views import head_doctor,intersection,total_surgeries

urlpatterns = [
    path('patients/without-insurance/', patients_without_insurance, name='patients_without_insurance'),
    path('doctors/with-more-appointments/', doctors_with_more_appointments, name='doctors_with_more_appointments'),
    path('surgery/update-surgery-status',update_surgery_status, name="update_surgery_status"),
    path('insuarance/retrieve-list',retrieve_list, name="retrieve_list"),
    path('department/dept-three-drs',dept_three_drs, name="dept_three_drs"),
    path('patients/patients-with-prescriptions', patients_with_prescriptions, name="patients_with_prescriptions"),
    path('patients/bulk-create-appointments', bulk_create_appointments, name="bulk_create_appointments"),
    path('prescription/retrieve-prescriptions', retrieve_prescriptions, name="retrieve_prescriptions"),
    path('insuarance/retrieve-app-MassMutual', retrieve_app_MassMutual, name="retrieve_app_MassMutual"),
    path('appointment/update-priority', update_priority, name='update_priority'),
    path("doctor/retrieve-dr-id", retrieve_dr_id, name="retrieve_dr_id"),
    path("patients/patients-union", patients_union , name="patients_union"),
    path("doctors/doctors-app-pres", doctors_app_pres , name="patients_union"),
    path("patients/patients-doctors", patients_doctors , name="patients_doctors"),
    path("doctor/doctor-specializations", doctor_specializations , name="doctor_specializations"),
    path("prescrition/pain-killer", prescription_pain_killer , name="prescription_pain_killer"),
    path("doctor/doctor-name", doctors_names , name="doctors_names"),
    path("patient/patiente-with-insurance", patiente_with_insurance , name="patiente_with_insurance"),
    path("doctor/fetch-doctors", fetch_doctors , name="fetch_doctors"),
    path("appointment/appointments-thirty-days", appointments_thirty_days , name="appointments_thirty_days"),
    path("patient/oldest-youngest-patients", oldest_youngest_patients , name="oldest_youngest_patients"),
    path("dept/dept-doctors", dept_doctors , name="dept_doctors"),
    path("appointments/cardiology-appointments", cardiology_appointments , name="cardiology_appointments"),
    path("appointments/difference", difference , name="difference"),
    path("department/head-doctor", head_doctor , name="head_doctor"),
    path("patients/intersection", intersection , name="intersection"),
    path("surgery/total-surgeries", total_surgeries , name="total_surgeries"),

    
]