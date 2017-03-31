# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='phone',
        ),
        migrations.AddField(
            model_name='shop',
            name='phones',
            field=models.ManyToManyField(to='places.Phone'),
        ),
    ]
