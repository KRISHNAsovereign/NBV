# Generated by Django 4.1.3 on 2023-08-22 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0012_remove_event_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='event_img/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.event')),
            ],
        ),
    ]