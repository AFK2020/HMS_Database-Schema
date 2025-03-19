from django.db import models
from myapp.constants import GenderType, AppointmentStatus, DoctorType, AppointmentType
from myapp.customfield import CustomPhoneNumberField



class Department(models.Model):
    name = models.CharField(max_length=255)
    head_doctor = models.OneToOneField("myapp.Doctor", related_name='dept_dr_id',verbose_name=("Head Doctor"), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    type = models.IntegerField(choices=DoctorType.choices(), default=DoctorType.PRIMARY_CARE)
    email = models.EmailField(max_length=255, verbose_name="Email Address")
    ph_number = CustomPhoneNumberField(verbose_name="Phone Number")
    department = models.ForeignKey(Department, verbose_name="Department Id", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Insuarance(models.Model):
    patient = models.OneToOneField("myapp.Patient", verbose_name=("Patient Name"), on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255)
    coverage_details = models.TextField(null=True,blank=True)

        
    def __str__(self):
        return self.provider




class Surgery(models.Model):
    patient = models.ForeignKey("myapp.Patient", verbose_name="Patient" , on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Doctor", on_delete=models.SET_NULL, null=True, blank=True)
    surgery_date = models.DateTimeField()
    surgery_type = models.CharField(max_length= 255)
    notes = models.TextField(null=True , blank= True)

        
    def __str__(self):
        return self.surgery_type





class Prescription(models.Model):
    appointment = models.OneToOneField(
                                    "myapp.Appointment",
                                    on_delete= models.CASCADE,
                                    verbose_name="Appointment Date",
                                    related_name= 'pres_app_id', 
                                    unique=True
                                    )
    doctor = models.ForeignKey(Doctor, verbose_name="Doctor",related_name='pres_dr_id', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.appointment




class Appointment(models.Model):
    patient_name = models.ForeignKey("myapp.Patient", verbose_name="Patient", related_name= 'app_p_id', on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, verbose_name="Doctor",related_name='app_dr_id', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.IntegerField(choices=AppointmentStatus.choices(),default=AppointmentStatus.SCHEDULED)
    type = models.IntegerField(choices=AppointmentType.choices(), default=AppointmentType.LOW)
    notes = models.TextField(blank=True, null=True)

        
    def __str__(self):
        return f"{self.patient} : {self.appointment_date}"




class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.IntegerField(choices=GenderType.choices(),default=GenderType.MALE)
    address = models.TextField(null=True, blank=True)
    ph_number = CustomPhoneNumberField(verbose_name="Phone Number")
    email = models.EmailField(max_length=255, null=True, blank=True)
    appointments = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ManyToManyField(Doctor, blank=True)

    def __str__(self):
        return self.name
    
