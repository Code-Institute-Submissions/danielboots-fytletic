# Generated by Django 3.1.6 on 2021-03-28 14:32

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0017_auto_20210328_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='gym_owner_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='street_address1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
