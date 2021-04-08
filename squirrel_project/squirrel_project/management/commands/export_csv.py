import csv

from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel

class Command(BaseCommand):
    '''
    This class creates custom commands
    We are using it to export the squirrel data 
    to a csv
    '''


    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Squirrels._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in Squirrels.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            f.close()