# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150121_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
