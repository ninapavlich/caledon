# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminappgroup',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='csspackage',
            old_name='file_source_content',
            new_name='generated_file_minified',
        ),
        migrations.RenameField(
            model_name='jspackage',
            old_name='file_source_content',
            new_name='generated_file_minified',
        ),
        migrations.AddField(
            model_name='adminappgroup',
            name='open_by_default',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='adminappgroup',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='adminapplink',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='adminlink',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='adminsidebar',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='csspackage',
            name='generated_file_source',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='csspackage',
            name='needs_render',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jspackage',
            name='generated_file_source',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='jspackage',
            name='needs_render',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legacyurl',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=255, null=True, verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='adminappgroup',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='adminapplink',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='adminlink',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='adminsidebar',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='csspackage',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='cssresource',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='cssresource',
            name='compiler',
            field=models.CharField(default=b'css', max_length=255, verbose_name=b'Compiler / Preprocessor', choices=[(b'css', b'CSS (None)'), (b'scss', b'SASS')]),
        ),
        migrations.AlterField(
            model_name='jspackage',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='jsresource',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='legacyurl',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='legacyurlreferer',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
