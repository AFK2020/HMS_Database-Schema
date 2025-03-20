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
    search_fields = ("provider",)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name__name","appointment_date",)
    list_filter = ["appointment_date"]
    search_fields = ("appointment_date",)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','gender')
    list_filter = ["doctor__name"]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Surgery)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Prescription)
admin.site.register(Insuarance,InsuranceAdmin)