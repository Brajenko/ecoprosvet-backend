# Generated by Django 5.1.1 on 2024-09-19 01:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_videofile_remove_video_filepond_video_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='filepond',
            field=models.FileField(max_length=255, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm'])]),
        ),
    ]
