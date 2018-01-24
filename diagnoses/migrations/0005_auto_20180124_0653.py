# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-24 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20180121_2200'),
        ('diagnoses', '0004_auto_20180124_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labtest',
            name='diagnosis',
        ),
        migrations.AddField(
            model_name='labtest',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
            preserve_default=False,
        ),
    ]
