# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='media',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='media',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='media',
            name='tags',
        ),
        migrations.AddField(
            model_name='image',
            name='file_modified_date',
            field=models.DateTimeField(null=True, verbose_name='File Modified Date', blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='media',
            name='file_modified_date',
            field=models.DateTimeField(null=True, verbose_name='File Modified Date', blank=True),
        ),
        migrations.AddField(
            model_name='media',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='mediatag',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='mediatag',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
