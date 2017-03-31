# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20151210_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='phones',
        ),
        migrations.AddField(
            model_name='place',
            name='phones',
            field=models.ManyToManyField(to='places.Phone', blank=True, null=True),
        ),
    ]
