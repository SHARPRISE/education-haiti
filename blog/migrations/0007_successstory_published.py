# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
