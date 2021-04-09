import csv
import datetime

from django.core.management.base import BaseCommand, CommandError
from .models import Squirrel




class Command(BaseCommand):
    '''
    This class creates custom commands
    We are using it to import the squirrel data 
    from a csv
    '''

    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']

        try:
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for i in reader:
                    s = Squirrel(
                        x = i['X'],
                        y = i['Y'],
                        unique_squirrel_id = i['Unique Squirrel ID'],
                        shift = i['Shift'],
                        date = datetime.date(int(i['Date'][-4:]),int(i['Date'][:2]),int(i['Date'][2:4])),
                        age = i['Age'],
                        primary_fur_color = i['Primary Fur Color'],
                        location = i['Location'],
                        specific_location = i['Specific Location'],
                        running = i['Running'].upper(),
                        chasing = i['Chasing'].upper(),
                        climbing = i['Climbing'].upper(),
                        eating = i['Eating'].upper(),
                        foraging = i['Foraging'].upper(),
                        other_activities = i['Other Activities'],
                        kuks = i['Kuks'].upper(),
                        quaas = i['Quaas'].upper(),
                        moans = i['Moans'].upper(),
                        tail_flags = i['Tail flags'].upper(),
                        tail_twitches = i['Tail twitches'].upper(),
                        approaches = i['Approaches'].upper(),
                        indifferent = i['Indifferent'].upper(),
                        runs_from = i['Runs from'].upper(),
                        )
                    s.save()
        except csv.Error as e:
            print(f'there is something wrong with {reader.line_num}')
