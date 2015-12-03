# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20151202_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_type',
        ),
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.ManyToManyField(to='places.PlaceType'),
        ),
    ]
