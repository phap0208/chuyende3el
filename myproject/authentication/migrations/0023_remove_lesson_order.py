# Generated by Django 4.2.6 on 2023-10-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_remove_quiz_course_delete_question_delete_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='order',
        ),
    ]