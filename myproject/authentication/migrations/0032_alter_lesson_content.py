# Generated by Django 4.2.6 on 2023-10-17 00:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0031_alter_question_text_alter_test_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
