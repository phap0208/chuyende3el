# Generated by Django 4.2.6 on 2023-11-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0063_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
