# Generated by Django 5.1.1 on 2024-09-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_duration_event_end_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventImages',
            new_name='EventImage',
        ),
    ]
