# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20151202_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_title', models.CharField(max_length=100)),
                ('shop_website', models.CharField(max_length=200)),
                ('shop_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='place_address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='place_discription',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='place_shop',
            field=models.ForeignKey(blank=True, to='places.Shop', null=True),
        ),
    ]
