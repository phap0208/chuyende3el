# Generated by Django 4.2.6 on 2023-10-29 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0055_alter_test_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='test',
            name='start_time',
        ),
    ]
