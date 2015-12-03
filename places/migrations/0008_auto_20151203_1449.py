# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20151203_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placetype',
            old_name='place_type_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='placetype',
            old_name='place_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='place',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
