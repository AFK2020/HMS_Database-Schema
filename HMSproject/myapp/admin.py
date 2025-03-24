from django.contrib import admin
from myapp.models import Insuarance, Department,Doctor,Appointment,Surgery,Patient,Prescription
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ["name"]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name","specialization")
    list_filter = ["specialization"]

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("provider",)
    list_filter = ["patient__name"]
    # search_fields = ("provider",)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name__name","appointment_date","doctor__name")
    list_filter = ["appointment_date", "doctor__name","status"]
    # search_fields = ("appointment_date",)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','gender','age')
    list_filter = ["doctor__name"]


class SurgeryAdmin(admin.ModelAdmin):
    list_display =( 'surgery_type','patient__name', 'doctor__name')
    list_filter =['patient__name', 'doctor__department__name']


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("appointment__patient_name", "appointment__appointment_date","doctor__name")

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Surgery,SurgeryAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Insuarance,InsuranceAdmin)