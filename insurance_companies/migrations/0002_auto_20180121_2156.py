# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-21 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='contact_phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]