# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20171210_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='sub_student_FK',
        ),
    ]
