# Generated by Django 4.2.6 on 2023-10-28 03:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0047_alter_lesson_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]