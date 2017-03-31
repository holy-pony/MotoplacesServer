# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20151203_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='pub_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_discription',
            new_name='discription',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_lng',
            new_name='lng',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_shop',
            new_name='shop',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='place_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_website',
            new_name='website',
        ),
        migrations.RemoveField(
            model_name='place',
            name='place_type',
        ),
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.ManyToManyField(to='places.PlaceType', related_name='places_type_rel'),
        ),
    ]
