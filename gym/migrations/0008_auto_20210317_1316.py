# Generated by Django 3.1.6 on 2021-03-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_auto_20210317_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='video',
            new_name='video_1',
        ),
        migrations.AddField(
            model_name='gym',
            name='video_2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='video_3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='video_4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='video_5',
            field=models.URLField(blank=True, null=True),
        ),
    ]
