# Generated by Django 4.1.4 on 2023-10-14 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonProject', '0009_rename_complete_task_complete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Complete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='User',
        ),
    ]
