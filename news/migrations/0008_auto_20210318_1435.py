# Generated by Django 3.1.6 on 2021-03-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_post_categorys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorys',
            new_name='categories',
        ),
    ]