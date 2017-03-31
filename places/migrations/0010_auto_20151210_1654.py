# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20151210_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='date',
            new_name='pub_date',
        ),
    ]
