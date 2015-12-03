# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='place_lng',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
