# Generated by Django 4.2.6 on 2023-10-11 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_remove_test_course_test_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.lesson'),
        ),
    ]