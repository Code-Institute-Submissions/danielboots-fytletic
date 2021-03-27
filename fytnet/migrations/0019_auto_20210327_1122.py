# Generated by Django 3.1.6 on 2021-03-27 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fytnet', '0018_auto_20210327_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='email',
            field=models.CharField(default='fighter@fytletic.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='fighter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='nick_name',
            field=models.CharField(default='Fytnet PRO Fighter', max_length=50),
        ),
    ]