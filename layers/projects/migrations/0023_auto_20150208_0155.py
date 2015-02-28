# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20150206_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(default=b'submit_idea', max_length=250, null=True, blank=True, choices=[(b'submit_idea', b'Submit Idea'), (b'design_center', b'Design Center'), (b'manufacturing', b'Manufacturing'), (b'Shipping', b'Shipping'), (b'Arrived', b'Completed Order')]),
            preserve_default=True,
        ),
    ]
