# Generated by Django 3.1.7 on 2021-04-13 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20210412_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='UNIQUE_SQUIRREL_ID',
            new_name='unique_squirrel_id',
        ),
    ]
