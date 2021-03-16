# Generated by Django 3.1.6 on 2021-03-16 17:03

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20210316_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='photo_3',
            new_name='gym_photo_main',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='profile_photo_main',
        ),
        migrations.AddField(
            model_name='gym',
            name='country',
            field=django_countries.fields.CountryField(default='DEFAULT', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gym',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='street_address1',
            field=models.CharField(default='DEFAULT ADDRESS', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gym',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='town_or_city',
            field=models.CharField(default='DEFAULT', max_length=40),
            preserve_default=False,
        ),
    ]
