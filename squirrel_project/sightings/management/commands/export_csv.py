import csv
import sys

from django.core.management import BaseCommand, CommandError
from sightings.models import Squirrel

class Command(BaseCommand):
    '''
    This class creates custom commands
    We are using it to export the squirrel data 
    to a csv
    '''


    def add_arguments(self, parser):
        parser.add_argument('path', type=str, nargs='*')

    def handle(self, path, **options):
        fields = Squirrel._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in Squirrel.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            f.close()