# Generated by Django 4.2.6 on 2023-10-23 01:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0046_alter_test_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
