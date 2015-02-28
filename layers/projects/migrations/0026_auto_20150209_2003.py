# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_project_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
