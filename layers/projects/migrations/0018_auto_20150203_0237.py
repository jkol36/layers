# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20150203_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(default=b'submit_idea', max_length=250, null=True, blank=True, choices=[(b'Submit Idea', b'Submit Idea'), (b'Design Center', b'Design Center'), (b'Shipping', b'Shipping'), (b'Complete', b'Completed Order')]),
            preserve_default=True,
        ),
    ]
