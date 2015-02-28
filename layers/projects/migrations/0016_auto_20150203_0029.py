# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20150203_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='designer',
            new_name='designers',
        ),
    ]
