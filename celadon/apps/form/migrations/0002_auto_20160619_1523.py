# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldentry',
            options={'ordering': ['form_field__order'], 'verbose_name': 'Field Entry', 'verbose_name_plural': 'Field Entries'},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'verbose_name': 'Forms', 'verbose_name_plural': 'Forms'},
        ),
        migrations.AlterModelOptions(
            name='formentry',
            options={'verbose_name': 'Form Entry', 'verbose_name_plural': 'Form Entries'},
        ),
        migrations.AlterModelOptions(
            name='formentrystatus',
            options={'verbose_name': 'Form Entry Status', 'verbose_name_plural': 'Form Entry Statuses'},
        ),
        migrations.AlterModelOptions(
            name='formentrytag',
            options={'verbose_name': 'Form Entry Tag', 'verbose_name_plural': 'Form Entry Tags'},
        ),
        migrations.AlterModelOptions(
            name='formfield',
            options={'verbose_name': 'Form Field', 'verbose_name_plural': 'Form Fields'},
        ),
        migrations.RemoveField(
            model_name='formfield',
            name='max_time',
        ),
        migrations.RemoveField(
            model_name='formfield',
            name='min_time',
        ),
        migrations.AddField(
            model_name='form',
            name='third_party_id',
            field=models.CharField(help_text=b'An identifier to integrate the form with another system', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='form',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='formentrystatus',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='formentrytag',
            name='title_path',
            field=models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='equal_to_error_message',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='max_datetime',
            field=models.DateTimeField(help_text=b'', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='max_height',
            field=models.IntegerField(help_text=b'Applies to image uploads', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='max_size',
            field=models.IntegerField(help_text=b'Applies to image and file uploads, measure in MB; e.g. 5000 is 5GB, 0.5 is 500KB', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='max_width',
            field=models.IntegerField(help_text=b'Applies to image uploads', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='min_datetime',
            field=models.DateTimeField(help_text=b'', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='min_height',
            field=models.IntegerField(help_text=b'Applies to image uploads', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='min_size',
            field=models.IntegerField(help_text=b'Applies to image and file uploads, measured in MB; e.g. 5000 is 5GB, 0.5 is 500KB', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='min_width',
            field=models.IntegerField(help_text=b'Applies to image uploads', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='pattern_error_message',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='formfield',
            name='third_party_id',
            field=models.CharField(help_text=b'An identifier to integrate the form with another system', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fieldentry',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='email_admin_override',
            field=models.CharField(help_text=b'Separate email addresses with comma, semi-color or space. Leave blank to send to default email address (info@celadon.com)', max_length=255, null=True, verbose_name='Admins to email on submission', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='extra_css_classes',
            field=models.CharField(help_text=b'Adds custom css classes into the form template.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='form_action',
            field=models.CharField(default=b'form-page', help_text=b'Defines whether to display this form on its own page with its own URL, or whether to embed it on another page elsehwere in the site. NOTE: Several of the subsections below only apply if the form action is a standalone form.', max_length=255, choices=[(b'form-page', 'Standalone Form'), (b'embedded-page', 'Form Embedded in Page')]),
        ),
        migrations.AlterField(
            model_name='form',
            name='form_create_message',
            field=models.CharField(help_text=b'Message to show user when they successfully submit the form.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='form_error_message',
            field=models.CharField(help_text=b'Global message to show user when there is an error in the form. NOTE: Individual fields have separate error messages.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='form_update_message',
            field=models.CharField(help_text=b'Message to show user when they successfully update the form. NOTE: Form must be editable to allow users to update the form.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_editable',
            field=models.BooleanField(default=False, help_text=b'Allows user to update the entry. NOTE: If this is checked, unless you also require a logged in user on the form, anyone with the correct URL can later update the entry. Therefore it is recommended that you use this in conjunction with requiring a logged in user.'),
        ),
        migrations.AlterField(
            model_name='form',
            name='redirect_url_on_submission',
            field=models.CharField(help_text=b'When a form is submitted you may override where the user is redirected.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='required_logged_in_user',
            field=models.BooleanField(default=False, help_text=b'Requires user to log in or create an account before filling out form. NOTE: This should only be turned on if you have enabled user registration on the site.'),
        ),
        migrations.AlterField(
            model_name='form',
            name='submit_label',
            field=models.CharField(default=b'Submit', help_text=b'Label on the submit button.', max_length=255),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formentrystatus',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formentrytag',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='error_message',
            field=models.CharField(help_text=b'Message to display when this field is invalid.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='extra_css_classes',
            field=models.CharField(help_text=b'Adds custom css classes onto the form field in the template.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='hide',
            field=models.BooleanField(default=False, help_text=b'Hide field from form without deleting and data entered by users. Use this instead of deleting a form field.'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='is_required',
            field=models.BooleanField(default=False, help_text=b'If this field is required, a value of some sort is needed for the user to submit the form. See the advanced validation options to apply more specific validation parameters.'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='pattern',
            field=models.CharField(help_text=b'Match a value or validate file types (e.g. .*\\.txt|.*\\.pdf|.*\\.doc)', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='type',
            field=models.CharField(help_text=b'Fill in choices field (in advanced options) for select fields. Fill in content field for instructions. WARNING: Only use password and secure file in conjunction with HTTPS.', max_length=255, choices=[(b'text-field', 'Single Line Text Field'), (b'email-field', 'Email Field'), (b'url-field', 'URL Field'), (b'integer-field', 'Integer Field'), (b'number-field', 'Number Field'), (b'text-area', 'Multiple Lines Text Area'), (b'boolean-checkboxes', 'Single Checkbox'), (b'boolean-toggle', 'Toggle'), (b'select-dropdown', 'Select with Dropdown'), (b'select-radio-buttons', 'Select with Radio Buttons'), (b'select-buttons', 'Select with Buttons'), (b'select-image', 'Select Image'), (b'select-multiple-checkboxes', 'Select Multiple with Checkboxes'), (b'select-multiple-autosuggest', 'Select Multiple with Autosuggest'), (b'select-multiple-horizontal', 'Select Multiple with Horizontal Lists'), (b'select-multiple-buttons', 'Select Multiple with Buttons'), (b'select-multiple-images', 'Select Multiple Images'), (b'comma-separated-list', 'List of Items'), (b'file', 'File'), (b'secure-file', 'Secure File'), (b'image', 'Image'), (b'date', 'Date'), (b'time', 'Time'), (b'date-time', 'Date and Time'), (b'score', 'Score'), (b'range', 'Range'), (b'number-slider', 'Number on a Slider'), (b'password', 'Password'), (b'form-instructions', 'Form Instructions'), (b'form-divider', 'Form Divider'), (b'form-step', 'Form Step'), (b'hidden-field', 'Hidden Field'), (b'honeypot-field', 'Honeypot Field')]),
        ),
    ]
