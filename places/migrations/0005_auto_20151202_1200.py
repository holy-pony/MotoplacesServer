# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20151130_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_type', models.CharField(max_length=16)),
                ('place_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='place_lat',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.ForeignKey(default=1, to='places.PlaceType'),
            preserve_default=False,
        ),
    ]
