# Generated by Django 3.1.6 on 2021-03-27 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fytnet', '0017_auto_20210327_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='fighter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
