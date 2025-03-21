from django.urls import path
from myapp.views import patients_without_insurance,doctors_with_more_appointments,update_surgery_status
from myapp.views import retrieve_list,dept_three_drs, patients_with_prescriptions,bulk_create_appointments,retrieve_prescriptions
from myapp.views import retrieve_app_MassMutual,update_priority, retrieve_dr_id,patients_union,doctors_app_pres

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

    
]