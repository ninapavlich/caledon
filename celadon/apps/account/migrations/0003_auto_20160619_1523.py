# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20151119_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='css_classes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra css classes to add to the item', null=True, verbose_name='CSS Classes'),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='extra_attributes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra attributes to add to the item', null=True, verbose_name='Extra Attributes'),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='target',
            field=models.CharField(default=b'_self', help_text=b'', max_length=255, verbose_name='Target', choices=[(b'_blank', '_blank'), (b'_self', '_self'), (b'_parent', '_parent'), (b'_top', '_top')]),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_1',
            field=models.CharField(max_length=30, null=True, verbose_name='Street Address 1', blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_2',
            field=models.CharField(max_length=30, null=True, verbose_name='Street Address 2', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='organizationmember',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='socialcontactlink',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='usergroupmember',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
