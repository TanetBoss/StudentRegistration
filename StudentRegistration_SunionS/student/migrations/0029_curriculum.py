# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0028_lecturerresearch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cCurriculum', models.CharField(max_length=30)),
                ('cur_dep_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Department')),
            ],
        ),
    ]
