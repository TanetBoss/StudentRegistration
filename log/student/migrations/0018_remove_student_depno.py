# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20171210_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='DepNo',
        ),
    ]