from django.contrib import admin
from myapp.models import Department,Doctor,Appointment,Surgery,Patient,Prescription
# Register your models here.



admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Surgery)
admin.site.register(Patient)
admin.site.register(Prescription)