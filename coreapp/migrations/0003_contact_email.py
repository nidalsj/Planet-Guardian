# Generated by Django 5.0.1 on 2024-01-23 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
