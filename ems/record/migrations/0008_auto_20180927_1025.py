# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0007_auto_20180926_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='nhis_charge',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='tax',
            field=models.IntegerField(default=2),
        ),
    ]
