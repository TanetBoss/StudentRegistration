# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0031_lecturer_lecturerdegree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='LecturerRating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
