# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20160612_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='mentees',
        ),
        migrations.DeleteModel(
            name='Mentee',
        ),
    ]