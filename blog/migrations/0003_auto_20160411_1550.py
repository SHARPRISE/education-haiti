# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160406_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Posted on'),
        ),
    ]
