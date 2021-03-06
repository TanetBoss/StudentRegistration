# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20171208_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectID', models.CharField(max_length=10)),
                ('SubjectName', models.CharField(max_length=30)),
                ('Section', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Degree',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Tel',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='StudentID',
            field=models.CharField(default='DEF', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='StudentName',
            field=models.CharField(default='DEF', max_length=30),
        ),
        migrations.AddField(
            model_name='subject',
            name='subjectFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
