# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20171210_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
