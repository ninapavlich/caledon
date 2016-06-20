# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celadon', '0005_auto_20160619_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winningteam',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='matchlogs',
            name='affected_player',
            field=models.ForeignKey(related_name='player', to='celadon.Player', null=True),
        ),
        migrations.AlterField(
            model_name='matchlogs',
            name='player',
            field=models.ForeignKey(to='celadon.Player', null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_match',
            field=models.ForeignKey(to='celadon.Match', null=True),
        ),
    ]
