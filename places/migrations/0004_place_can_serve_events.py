# Generated by Django 5.1.1 on 2024-09-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_photos_place_address_placesimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='can_serve_events',
            field=models.BooleanField(default=False),
        ),
    ]
