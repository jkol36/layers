# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150112_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(related_name='client', default=False, blank=True, to='profiles.Layers_Profile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='designer',
            field=models.ForeignKey(related_name='designer', default=False, blank=True, to='profiles.Layers_Profile', null=True),
            preserve_default=True,
        ),
    ]
