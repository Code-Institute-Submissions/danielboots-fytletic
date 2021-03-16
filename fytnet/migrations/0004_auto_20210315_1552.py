# Generated by Django 3.1.6 on 2021-03-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fytnet', '0003_auto_20210315_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='image',
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='profile_photo_main',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
    ]