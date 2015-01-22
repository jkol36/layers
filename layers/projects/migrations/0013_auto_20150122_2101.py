# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20150122_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget_max',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='budget_min',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
