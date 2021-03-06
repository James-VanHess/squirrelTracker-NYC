import csv
import sys

from django.core.management import BaseCommand, CommandError
from django.apps import apps
from sightings.models import Squirrel


class Command(BaseCommand):
    '''
    This class creates custom commands
    We are using it to export the squirrel data 
    to a csv
    '''

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *app_labels, **options):
         with open(options['csv_file'], 'w') as fp:
            model = apps.get_model('sightings', 'Squirrel')
            field_names = [f.name for f in model._meta.fields]
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)

            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])
                print('Data exported successfully from sightings db')