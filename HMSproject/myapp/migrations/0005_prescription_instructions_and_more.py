# Generated by Django 5.1.7 on 2025-03-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_appointment_status_alter_doctor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medicine_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
