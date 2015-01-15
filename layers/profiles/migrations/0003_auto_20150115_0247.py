# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_layers_profile_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='layers_profile',
            name='newsletter',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layers_profile',
            name='notification_emails',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
