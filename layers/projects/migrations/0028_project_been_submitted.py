# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20150213_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='been_submitted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
