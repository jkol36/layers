# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='budget',
            new_name='budget_max',
        ),
        migrations.AddField(
            model_name='project',
            name='budget_min',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
