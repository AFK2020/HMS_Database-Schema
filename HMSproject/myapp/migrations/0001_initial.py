# Generated by Django 5.1.7 on 2025-03-18 15:50

import django.db.models.deletion
import myapp.constants
import myapp.customfield
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'PRIMARY_CARE'), (2, 'CONSULTANT'), (3, 'SPECIALIST')], default=myapp.constants.DoctorType['PRIMARY_CARE'])),
                ('email', models.EmailField(max_length=255, verbose_name='Email Address')),
                ('ph_number', myapp.customfield.CustomPhoneNumberField(max_length=15, verbose_name='Phone Number')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department', verbose_name='Department Id')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='head_doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dept_dr_id', to='myapp.doctor', verbose_name='Head Doctor'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'SCHEDULED'), (2, 'COMPLETED'), (3, 'CANCELLED')], default=myapp.constants.AppointmentStatus['SCHEDULED'])),
                ('notes', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_dr_id', to='myapp.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], default=myapp.constants.GenderType['MALE'])),
                ('address', models.TextField(blank=True, null=True)),
                ('ph_number', myapp.customfield.CustomPhoneNumberField(max_length=15, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('appointments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.appointment')),
                ('doctor', models.ManyToManyField(to='myapp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Insuarance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=255)),
                ('policy_number', models.CharField(max_length=255)),
                ('coverage_details', models.TextField(blank=True, null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient', verbose_name='Patient Name')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_p_id', to='myapp.patient', verbose_name='Patient'),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pres_app_id', to='myapp.appointment', verbose_name='Appointment Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pres_dr_id', to='myapp.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surgery_date', models.DateTimeField()),
                ('surgery_type', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.patient', verbose_name='Patient')),
            ],
        ),
    ]
