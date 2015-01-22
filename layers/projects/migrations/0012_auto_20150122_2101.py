# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20150122_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='budget_max',
        ),
        migrations.RemoveField(
            model_name='project',
            name='budget_min',
        ),
    ]
