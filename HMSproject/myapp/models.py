from django.db import models
from myapp.constants import GenderType, AppointmentStatus, DoctorType, AppointmentType
from myapp.customfield import CustomPhoneNumberField
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=255)
    head_doctor = models.OneToOneField(
        "myapp.Doctor",
        related_name="dept_dr_id",
        verbose_name=("Head Doctor"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    type = models.CharField( max_length= 100,
        choices=DoctorType.choices(), default=DoctorType.PRIMARY_CARE
    )
    email = models.EmailField(max_length=255, verbose_name="Email Address")
    ph_number = CustomPhoneNumberField(verbose_name="Phone Number")
    department = models.ForeignKey(
        Department,
        verbose_name="Department Id",
        on_delete=models.CASCADE,
        related_name= "dr_to_dept",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Insuarance(models.Model):
    patient = models.ForeignKey(
        "myapp.Patient",
        verbose_name=("Patient Name"),
        on_delete=models.CASCADE,
        related_name="insuarance_pt",
    )
    provider = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255)
    coverage_details = models.TextField(blank=True)

    def __str__(self):
        return self.provider


class Surgery(models.Model):
    patient = models.ForeignKey(
        "myapp.Patient",
        verbose_name="Patient",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name= "surgery_patient"
    )
    doctor = models.ForeignKey(
        Doctor, verbose_name="Doctor", on_delete=models.SET_NULL, null=True, blank=True,
        related_name="surgery_doctor"
    )
    surgery_date = models.DateTimeField()
    surgery_type = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.surgery_type

    class Meta:
        verbose_name_plural = "Surgeries"


class Prescription(models.Model):
    appointment = models.OneToOneField(
        "myapp.Appointment",
        on_delete=models.CASCADE,
        verbose_name="Appointment Name",
        related_name="pres_app_id",
        unique=True,
    )
    doctor = models.ForeignKey(
        Doctor,
        verbose_name="Doctor",
        related_name="pres_dr_id",
        on_delete=models.CASCADE,
    )
    medicine_details = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.appointment.id} {self.doctor.name}"


class Appointment(models.Model):
    patient_name = models.ForeignKey(
        "myapp.Patient",
        verbose_name="Patient",
        related_name="app_p_id",
        on_delete=models.CASCADE,
    )
    doctor = models.ForeignKey(
        Doctor,
        verbose_name="Doctor",
        related_name="app_dr_id",
        on_delete=models.CASCADE,
    )
    appointment_date = models.DateField()
    status = models.CharField( max_length=100,
        choices=AppointmentStatus.choices(), default=AppointmentStatus.SCHEDULED
    )
    type = models.CharField( max_length=100,
        choices=AppointmentType.choices(), default=AppointmentType.LOW
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name.name}: {self.type}"


class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=100, choices=GenderType.choices(), default=GenderType.MALE)
    address = models.TextField(null=True, blank=True)
    ph_number = CustomPhoneNumberField(verbose_name="Phone Number")
    email = models.EmailField(max_length=255, null=True, blank=True)
    appointments = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, null=True, blank=True, related_name="appoint_patient"
    )
    doctor = models.ManyToManyField(Doctor, blank=True, related_name="doctor_patients")

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.dob.year)
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )
        return age

    def __str__(self):
        return f"{self.name} : {self.age}"
