# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_calcsalary_companyinfo_documents_leaves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='name',
        ),
        migrations.RemoveField(
            model_name='records',
            name='document',
        ),
        migrations.AddField(
            model_name='documents',
            name='document_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.CharField(choices=[('select document to upload', 'select document to upload'), ('cv', 'cv'), ('birth_certificate', 'birth_certificate'), ('ssce_certificate', 'ssce_certificate'), ('OND_certificate', 'OND_certificate'), ('valid_ID_card', 'valid_ID_card'), ('first_degree_certificate', 'first_degree_certificate'), ('NYSC_certificate', 'NYSC_certificate'), ('MSc_certificate', 'MSc_certificate')], default='select document to upload', max_length=50),
        ),
    ]
