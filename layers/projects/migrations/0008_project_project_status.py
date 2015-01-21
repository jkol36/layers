# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150114_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, max_length=250, null=True, choices=[(b'submit_idea', b'submit_idea'), (b'Design Center', b'Design Center'), (b'Shipping', b'Shipping')]),
            preserve_default=True,
        ),
    ]
