# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-24 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0003_diagnosis_possible_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='possible_diagnosis',
            field=models.TextField(),
        ),
    ]
