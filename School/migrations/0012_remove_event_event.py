# Generated by Django 4.1.3 on 2023-08-22 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0011_event_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event',
        ),
    ]