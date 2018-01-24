# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-21 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_companies.InsuranceCompany'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=patients.models.patient_directory_path),
        ),
    ]