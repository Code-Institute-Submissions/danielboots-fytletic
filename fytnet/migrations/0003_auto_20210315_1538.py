# Generated by Django 3.1.6 on 2021-03-15 15:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fytnet', '0002_auto_20210315_1528'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fytnet',
            new_name='Fighter',
        ),
    ]
