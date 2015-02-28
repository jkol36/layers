# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20150203_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(related_name='client', default=None, blank=True, to='profiles.Layers_Profile', null=True),
            preserve_default=True,
        ),
    ]
