# Generated by Django 5.0.1 on 2024-01-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='timestamp',
            new_name='timeStamp',
        ),
    ]
