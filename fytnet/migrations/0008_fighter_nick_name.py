# Generated by Django 3.1.6 on 2021-03-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fytnet', '0007_fighter_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='nick_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
    ]
