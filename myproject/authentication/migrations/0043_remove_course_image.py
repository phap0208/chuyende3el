# Generated by Django 4.2.6 on 2023-10-21 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0042_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
    ]