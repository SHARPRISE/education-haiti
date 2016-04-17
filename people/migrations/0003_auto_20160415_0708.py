# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160415_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('A', 'mentor'), ('B', 'mentee')], default=('B', 'mentee'), max_length=1),
        ),
    ]
