# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150507_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
