# Generated by Django 4.2.6 on 2023-11-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0064_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course_images/'),
        ),
    ]