# Generated by Django 5.1.7 on 2025-03-20 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_insuarance_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuarance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insuarance_pt', to='myapp.patient', verbose_name='Patient Name'),
        ),
    ]
