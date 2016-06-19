# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celadon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-created_date'], 'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='matchlogs',
            options={'ordering': ['-created_date'], 'verbose_name': 'Match Log', 'verbose_name_plural': 'Match Logs'},
        ),
        migrations.AlterModelOptions(
            name='matchuser',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='match',
            name='matchid',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
