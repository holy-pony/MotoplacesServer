# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='question_text',
            new_name='place_title',
        ),
        migrations.RemoveField(
            model_name='place',
            name='pub_date',
        ),
    ]
