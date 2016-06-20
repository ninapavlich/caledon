# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celadon', '0003_auto_20160619_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('typeid', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created_date'],
                'verbose_name': 'Log Type',
                'verbose_name_plural': 'Log Types',
            },
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-created_date']},
        ),
        migrations.RemoveField(
            model_name='matchlogs',
            name='user',
        ),
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='mapname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='match_aborted',
            field=models.BooleanField(default='false'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='match_complete',
            field=models.BooleanField(default='true'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='winningteam',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchlogs',
            name='affected_player',
            field=models.ForeignKey(related_name='player', default='', to='celadon.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchlogs',
            name='logmessage',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchlogs',
            name='player',
            field=models.ForeignKey(default='', to='celadon.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchlogs',
            name='timestamp',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchuser',
            name='role',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='current_match',
            field=models.ForeignKey(default='', to='celadon.Match'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchlogs',
            name='logtype',
            field=models.ForeignKey(default='', to='celadon.LogType'),
            preserve_default=False,
        ),
    ]
