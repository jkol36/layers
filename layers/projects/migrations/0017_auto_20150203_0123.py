# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150202_2344'),
        ('projects', '0016_auto_20150203_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='project',
            name='designers',
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.OneToOneField(related_name='client', null=True, default=None, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='designer',
            field=models.OneToOneField(related_name='designer', null=True, default=None, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
    ]
