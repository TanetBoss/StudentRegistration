# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('adv_lec_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Lecturer')),
                ('adv_stu_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
