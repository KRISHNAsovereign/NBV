# Generated by Django 4.1.3 on 2023-08-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='classes',
            field=models.ManyToManyField(blank=True, to='School.subject'),
        ),
    ]