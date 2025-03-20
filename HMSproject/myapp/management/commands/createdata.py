from django.core.management.base import BaseCommand
import random
from random import randrange
from myapp.models import Patient,Department,Doctor,Appointment,Prescription,Surgery, Insuarance
from myapp.constants import GenderType,AppointmentStatus, DoctorType,AppointmentType
from faker import Faker
from django.utils import timezone
from datetime import datetime,timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Command information'

    def handle(self, *args, **options):
        @staticmethod
        def fake_department(n):
            departments=[]

            list_of_departments = [
                    "Emergency Department (ED)",
                    "Intensive Care Unit (ICU)",
                    "Surgical Department",
                    "General Surgery",
                    "Orthopedic Surgery",
                    "Neurosurgery",
                    "Cardiac Surgery",
                    "Pediatrics",
                    "Obstetrics and Gynecology (OB/GYN)",
                    "Radiology",
                    "X-ray",
                    "CT Scan",
                    "MRI",
                    "Ultrasound",
                    "Pathology",
                    "Pharmacy",
                    "Anesthesiology",
                    "Cardiology",
                    "Neurology",
                    "Oncology",
                    "Dermatology",
                    "Psychiatry",
                    "Physical Therapy",
                    "Nephrology (Kidney Care)",
                    "Gastroenterology",
                    "Hematology",
                    "Urology",
                    "Ophthalmology",
                    "ENT (Ear, Nose, and Throat)",
                    "Endocrinology",
                    "Infectious Disease",
                    "Pulmonology",
                    "Rheumatology",
                    "Laboratory"
                ]
            unique_dept = random.sample(list_of_departments, n)
            for dept_name in unique_dept:
                department_created = Department.objects.create(name = dept_name)
                
                departments.append(department_created)

            return departments
        
        @staticmethod
        def add_fake_doctors(departments,n):
            doctors = []

            doctor_specilization_department = {
                'Emergency Department (ED)': 'ER Doctor',
                'Intensive Care Unit (ICU)': 'Intensivist',
                'Surgical Department': 'Surgeon',
                'General Surgery': 'General Surgeon',
                'Orthopedic Surgery': 'Orthopedic Surgeon',
                'Neurosurgery': 'Neurosurgeon',
                'Cardiac Surgery': 'Cardiac Surgeon',
                'Pediatrics': 'Pediatrician',
                'Obstetrics and Gynecology (OB/GYN)': 'OB Gynecologist',
                'Radiology': 'Radiologist',
                'X-ray': 'Radiologic Technologist',
                'CT Scan': 'Radiologic Technologist',
                'MRI': 'Radiologic Technologist',
                'Ultrasound': 'Ultrasonographer',
                'Pathology': 'Pathologist',
                'Pharmacy': 'Pharmacist',
                'Anesthesiology': 'Anesthesiologist',
                'Cardiology': 'Cardiologist',
                'Neurology': 'Neurologist',
                'Oncology': 'Oncologist',
                'Dermatology': 'Dermatologist',
                'Psychiatry': 'Psychiatrist',
                'Physical Therapy': 'Physical Therapist',
                'Nephrology (Kidney Care)': 'Nephrologist',
                'Gastroenterology': 'Gastroenterologist',
                'Hematology': 'Hematologist',
                'Urology': 'Urologist',
                'Ophthalmology': 'Ophthalmologist',
                'ENT (Ear, Nose, and Throat)': 'ENT Specialist',
                'Endocrinology': 'Endocrinologist',
                'Infectious Disease': 'Infectious Disease Specialist',
                'Pulmonology': 'Pulmonologist',
                'Rheumatology': 'Rheumatologist',
                'Laboratory': 'Lab Technician'
            }
            
    
            for _ in range(n):
                department_name = random.choice(departments)
                specialize_in = doctor_specilization_department.get(department_name.name, 'ER Doctor')
                doctor = Doctor.objects.create(
                    name = fake.name(),
                    department = department_name,
                    specialization = specialize_in,
                    type = random.choice([x[0] for x in DoctorType.choices()]),
                    email = fake.email(),
                    ph_number = fake.ean(length=13),
                )
                doctors.append(doctor)
            return doctors
        
        @staticmethod
        def add_fake_patients(doctors,n):
            patients =[]
            for _ in range(n):
                patient= Patient.objects.create(
                    name = fake.name(),
                    dob = fake.date_between_dates(date_start=datetime(1920,1,1), date_end=datetime(2025,3,20)),
                    address = fake.address(),
                    gender = random.choice([x[0] for x in GenderType.choices()]),
                    email = fake.email(),
                    ph_number = fake.ean(length=13)
                )

                assigned_doctors = random.sample(doctors, random.randint(1, 3))  # Link 1 to 3 doctors
                patient.doctor.add(*assigned_doctors)  # Add doctors to the patient
                patients.append(patient)

            return patients

        @staticmethod
        def add_fake_appointment(patients,doctors,n):
            appointments = []
            start_date = datetime(2024, 1, 1)
            end_date = datetime(2025, 6, 20)
            for _ in range(n):
                appointment = Appointment.objects.create(
                    patient_name = random.choice(patients),
                    doctor = random.choice(doctors),
                    appointment_date = random_date(start_date,end_date),
                    status = random.choice([x[0] for x in AppointmentStatus.choices()]),
                    type = random.choice([x[0] for x in AppointmentType.choices()]),
                    notes = fake.text()
                    )
                appointments.append(appointment)

            return appointments

        @staticmethod
        def add_fake_surgeries(patients,doctors,n):

            surgery_types = [
                "Cardiac Surgery",
                "Orthopedic Surgery",
                "Neurosurgery",
                "Plastic Surgery",
                "General Surgery",
                "Bariatric Surgery",
                "Ophthalmic Surgery",
                "Pediatric Surgery",
                "Gastrointestinal Surgery",
                "Urological Surgery",
                "Gynecological Surgery",
                "Thoracic Surgery",
                "Vascular Surgery",
                "Transplant Surgery",
                "Cosmetic Surgery",
                "Laparoscopic Surgery",
                "Endoscopic Surgery",
                "Spinal Surgery",
                "Dental Surgery",
                "ENT Surgery (Ear, Nose, Throat)",
                "Maxillofacial Surgery",
                "Cancer Surgery",
                "Trauma Surgery",
                "Robotic Surgery",
                "Reconstructive Surgery",
                "Dermatologic Surgery",
                "Nephrectomy",
                "Hernia Surgery"
                ]

            for _ in range(n):
                naive_surgery_date = fake.date_time_between(start_date='-1y', end_date='now')
                surgery_date = timezone.make_aware(naive_surgery_date)

                Surgery.objects.create(
                    patient = random.choice(patients),
                    doctor = random.choice(doctors),
                    surgery_date = surgery_date,
                    surgery_type = random.choice(surgery_types),
                    notes = fake.text()
                )
        @staticmethod
        def add_fake_prescription(appointment,doctors,n):
            # unique_appointments = random.sample(appointment, 1)
            unique_appointments = random.sample(appointment,n) # get n unique appointments
            for appointment in unique_appointments:
                Prescription.objects.create(
                    appointment = appointment,
                    doctor = random.choice(doctors)
                )

        @staticmethod
        def add_fake_insurance(patients, n):
            insurance_companies = [
                    "State Farm",
                    "Geico",
                    "Progressive",
                    "Allstate",
                    "Nationwide",
                    "Liberty Mutual",
                    "Farmers Insurance",
                    "The Hartford",
                    "Travelers",
                    "American Family Insurance",
                    "Aetna",
                    "UnitedHealthcare",
                    "Cigna",
                    "Anthem",
                    "MetLife",
                    "Prudential",
                    "New York Life",
                    "Lincoln Financial Group",
                    "MassMutual",
                    "Chubb",
                    "Zurich",
                    "AXA",
                    "Allianz",
                    "Berkshire Hathaway",
                    "Zurich Insurance",
                    "Manulife Financial"
                ]
            unique_companies = random.sample(insurance_companies,n)
            for company in unique_companies:
                Insuarance.objects.create(
                    patient = random.choice(patients),
                    provider = company,
                    policy_number = random.randint(1111,9999),
                    coverage_details = fake.text()
                )


            # Function to generate a random date
        def random_date(start_date, end_date):
            # Calculate the difference between the two dates
            delta = end_date - start_date
            # Get a random number of days to add to the start date
            random_days = random.randint(0, delta.days)
            # Add the random number of days to the start date
            return start_date + timedelta(days=random_days)


        model = [ Patient, Department, Doctor, Appointment,Surgery, Prescription, Insuarance]

        for i in model:
            i.objects.all().delete()

        departments = fake_department(15)
        drs = add_fake_doctors(departments,25)
        pt = add_fake_patients(drs,100)
        app = add_fake_appointment(pt,drs,100)
        surgeries = add_fake_surgeries(pt,drs,41)
        insuarance = add_fake_insurance(pt,15)
        prescription = add_fake_prescription(app,drs,60)

       


            
