# Generated by Django 5.1.1 on 2024-09-19 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='organization_description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='organization_inn',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='organization_name',
        ),
    ]
