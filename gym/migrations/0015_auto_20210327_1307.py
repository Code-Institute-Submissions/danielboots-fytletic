# Generated by Django 3.1.6 on 2021-03-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0014_gym_gym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='email',
            field=models.CharField(default='gym@fytletic.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='gym',
            name='whatsapp',
            field=models.CharField(default='5555555555', max_length=50),
        ),
    ]