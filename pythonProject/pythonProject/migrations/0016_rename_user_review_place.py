# Generated by Django 4.1.4 on 2023-10-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonProject', '0015_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='place',
        ),
    ]
