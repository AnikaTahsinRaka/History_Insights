# Generated by Django 4.1.4 on 2023-10-14 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonProject', '0012_alter_task_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='User',
            new_name='user',
        ),
    ]