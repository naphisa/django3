# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0011_auto_20180927_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='total_salary_monthly',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='total_salary_yearly',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]