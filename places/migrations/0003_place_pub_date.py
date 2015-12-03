# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20151130_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 18, 35, 12, 289258, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
