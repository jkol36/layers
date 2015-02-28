# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150115_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layers_profile',
            name='newsletter',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='layers_profile',
            name='notification_emails',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='layers_profile',
            name='profile',
            field=models.OneToOneField(related_name='accounts', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
