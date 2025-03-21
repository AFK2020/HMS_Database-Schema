# Generated by Django 5.1.7 on 2025-03-20 15:41

import django.db.models.deletion
import myapp.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_insuarance_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(choices=[(1, 'SCHEDULED'), (2, 'COMPLETED'), (3, 'CANCELLED'), (4, 'MISSED')], default=myapp.constants.AppointmentStatus['SCHEDULED']),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dr_to_dept', to='myapp.department', verbose_name='Department Id'),
        ),
    ]
