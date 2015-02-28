# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20150202_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='client',
            new_name='clients',
        ),
    ]
