# Generated by Django 5.1.1 on 2024-09-19 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_questions_request_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='description',
        ),
    ]
