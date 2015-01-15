# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150112_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'/project_pics/', blank=True),
            preserve_default=True,
        ),
    ]
