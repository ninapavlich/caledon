# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celadon', '0004_auto_20160619_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='match',
            name='title',
        ),
    ]
