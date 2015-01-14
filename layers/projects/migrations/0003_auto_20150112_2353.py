# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('projects', '0002_auto_20150112_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profiles',
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(related_name='client', default=None, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='designer',
            field=models.ForeignKey(related_name='designer', default=None, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
    ]
