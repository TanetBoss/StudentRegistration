# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20171209_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='StudentID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='StudentName',
        ),
        migrations.AddField(
            model_name='student',
            name='DOB',
            field=models.CharField(default='DEF', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='Degree',
            field=models.CharField(default='DEG', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='Tel',
            field=models.CharField(default='TEL', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Department'),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='NAME', max_length=200),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
