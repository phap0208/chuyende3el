# Generated by Django 4.2.6 on 2023-10-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0037_test_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
