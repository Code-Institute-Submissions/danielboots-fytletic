# Generated by Django 3.1.6 on 2021-03-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_auto_20210316_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='image_test',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]