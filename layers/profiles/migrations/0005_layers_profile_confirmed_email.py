# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150202_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='layers_profile',
            name='confirmed_email',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
