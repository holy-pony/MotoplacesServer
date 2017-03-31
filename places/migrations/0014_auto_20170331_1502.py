# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_auto_20151210_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_title', models.CharField(max_length=200)),
                ('location_lat', models.FloatField()),
                ('location_lng', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='place',
            old_name='address',
            new_name='place_address',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='discription',
            new_name='place_discription',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='shop',
            new_name='place_shop',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='title',
            new_name='place_title',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='type',
            new_name='place_type',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='title',
            new_name='shop_title',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='website',
            new_name='shop_website',
        ),
        migrations.RemoveField(
            model_name='place',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='place',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='place',
            name='phones',
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_phone',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.AddField(
            model_name='place',
            name='place_position',
            field=models.OneToOneField(null=True, to='places.Location'),
        ),
    ]
