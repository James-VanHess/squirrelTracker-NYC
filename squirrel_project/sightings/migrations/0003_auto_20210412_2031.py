# Generated by Django 3.1.7 on 2021-04-13 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20210412_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='age',
            new_name='AGE',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='approaches',
            new_name='APPROACHES',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='chasing',
            new_name='CHASING',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='climbing',
            new_name='CLIMBING',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='date',
            new_name='DATE',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='eating',
            new_name='EATING',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='foraging',
            new_name='FORAGING',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='indifferent',
            new_name='INDIFFERENT',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='kuks',
            new_name='KUKS',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='x',
            new_name='LATITUDE',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='location',
            new_name='LOCATION',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='y',
            new_name='LONGITUDE',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='moans',
            new_name='MOANS',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='other_activities',
            new_name='OTHER_ACTIVITIES',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='primary_fur_color',
            new_name='PRIMARY_FUR_COLOR',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='quaas',
            new_name='QUAAS',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='running',
            new_name='RUNNING',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='runs_from',
            new_name='RUNS_FROM',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='shift',
            new_name='SHIFT',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='specific_location',
            new_name='SPECIFIC_LOCATION',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='tail_flags',
            new_name='TAIL_FLAGS',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='tail_twitches',
            new_name='TAIL_TWITCHES',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='unique_squirrel_id',
            new_name='UNIQUE_SQUIRREL_ID',
        ),
    ]