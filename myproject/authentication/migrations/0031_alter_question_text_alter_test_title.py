# Generated by Django 4.2.6 on 2023-10-17 00:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0030_alter_test_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]