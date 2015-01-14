# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='profiles',
            field=models.ManyToManyField(to='profiles.Layers_Profile', blank=True),
            preserve_default=True,
        ),
    ]
