# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20150122_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.OneToOneField(related_name='client', null=True, default=False, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='designer',
            field=models.OneToOneField(related_name='designer', null=True, default=False, blank=True, to='profiles.Layers_Profile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(default=b'submit_idea', max_length=250, null=True, blank=True, choices=[(b'submit_idea', b'Submit Idea'), (b'Design Center', b'Design Center'), (b'Shipping', b'Shipping'), (b'Complete', b'Completed Order')]),
            preserve_default=True,
        ),
    ]
