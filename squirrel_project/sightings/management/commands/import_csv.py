import csv
import datetime

from django.core.management import BaseCommand, CommandError

from sightings.models import Squirrel


# utility function
def str_to_bool(s):
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    else:
        # evil ValueError that doesn't tell you what the wrong value was
        raise ValueError("Wrong boolean value!")


def valid_age(s):
    if s not in (Squirrel.ADULT, Squirrel.JUVENILE):
        return "Unknown"
    return s


def valid_color(s):
    if s not in (Squirrel.CINNAMON, Squirrel.BLACK, Squirrel.GRAY):
        return "Unknown"
    return s

def valid_location(s):
    if s not in (Squirrel.ABOVE, Squirrel.GROUND):
        return "Unknown"
    return s



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            squirrel = Squirrel.objects.filter(
                unique_squirrel_id=item['Unique Squirrel ID'])
            if squirrel.exists():
                print(f"{item['Unique Squirrel ID']} already exists.")
                continue

            squirrel, created = Squirrel.objects.get_or_create(
                LONGITUDE=item['X'],
                LATITUDE=item['Y'],
                unique_squirrel_id=item['Unique Squirrel ID'],
                SHIFT=item['Shift'],
                DATE=datetime.datetime.strptime(
                    item['Date'].strip(), '%m%d%Y').date(),
                AGE=valid_age(item['Age']),
                PRIMARY_FUR_COLOR=valid_color(item['Primary Fur Color']),
                LOCATION=valid_location(item['Location']),
                SPECIFIC_LOCATION=item['Specific Location'],
                RUNNING=str_to_bool(item['Running']),
                CHASING=str_to_bool(item['Chasing']),
                CLIMBING=str_to_bool(item['Climbing']),
                EATING=str_to_bool(item['Eating']),
                FORAGING=str_to_bool(item['Foraging']),
                OTHER_ACTIVITIES=item['Other Activities'],
                KUKS=str_to_bool(item['Kuks']),
                QUAAS=str_to_bool(item['Quaas']),
                MOANS=str_to_bool(item['Moans']),
                TAIL_FLAGS=str_to_bool(item['Tail flags']),
                TAIL_TWITCHES=str_to_bool(item['Tail twitches']),
                APPROACHES=str_to_bool(item['Approaches']),
                INDIFFERENT=str_to_bool(item['Indifferent']),
                RUNS_FROM=str_to_bool(item['Runs from']),
            )
            if created:
                squirrel.save()
                print(
                    f"Squirrel {item['Unique Squirrel ID']} has been loaded.")
            else:
                raise ValueError("Wrong in data!")


# class Command(BaseCommand):
#     help = 'import data'

#     def add_arguments(self, parser):
#         parser.add_argument('path',type=str,help="csv file")

#     def handle(self, path, **options):
#         with open(path, 'r',encoding='UTF-8') as f:
#             reader = csv.reader(f)
#             next(reader)
#             for row in reader:
#                 _, created = Squirrel.objects.get_or_create(
#                     latitude = row[0],
#                     longitude= row[1],
#                     unique_squirrel_id = row[2],
#                     shift = row[4],
#                     date = row[5][4:8]+'-'+ row[5][0:2]+'-'+ row[5][2:4],
#                     age = row[7],
#                     primary_fur_color = row[8],
#                     location = row[12],
#                     specific_location = row[14],
#                     running = True if row[15].lower()=='true' else False,
#                     chasing = True if row[16].lower()=='true' else False,
#                     climbing = True if row[17].lower()=='true' else False,
#                     eating = True if row[18].lower()=='true' else False,
#                     foraging = True if row[19].lower()=='true' else False,
#                     other_activities = row[20],
#                     kuks = True if row[21].lower()=='true' else False,
#                     quaas = True if row[22].lower()=='true' else False,
#                     moans = True if row[23].lower()=='true' else False,
#                     tail_flags = True if row[24].lower()=='true' else False,
#                     tail_twitches = True if row[25].lower()=='true' else False,
#                     approaches = True if row[26].lower()=='true' else False,
#                     indifferent = True if row[27].lower()=='true' else False,
#                     runs_from = True if row[28].lower()=='true' else False,)

# # class Command(BaseCommand):
# #     '''
# #     This class creates custom commands
# #     We are using it to import the squirrel data 
# #     from a csv
# #     '''

# #     def add_arguments(self, parser):
# #         parser.add_argument('csv_file')
    
# #     def handle(self, *args, **options):
# #         with open(options['csv_file'], encoding='utf-8') as f:
# #             reader = csv.DictReader(f)
# #             data = list(reader)

# #             for i in data:
# #                 # s = Squirrel.objects.filter(unique_squirrel_id=i['Unique Squirrel ID'])
# #                 # if s.exists():
# #                 #     print(f'{unique_squirrel_id} already exists.')
# #                 #     continue

# #                 s, created = Squirrel.objects.get_or_create(
# #                     x = i['X'],
# #                     y = i['Y'],
# #                     unique_squirrel_id = i['Unique Squirrel ID'],
# #                     shift = i['Shift'],
# #                     date = datetime.date(int(i['Date'][-4:]),int(i['Date'][:2]),int(i['Date'][2:4])),
# #                     age = i['Age'],
# #                     primary_fur_color = i['Primary Fur Color'],
# #                     location = i['Location'],
# #                     specific_location = i['Specific Location'],
# #                     running = True if i['Running'].upper()=='true' else False,
# #                     chasing = True if i['Chasing'].upper()=='true' else False,
# #                     climbing = True if i['Climbing'].upper()=='true' else False,
# #                     eating = True if i['Eating'].upper()=='true' else False,
# #                     foraging = True if i['Foraging'].upper()=='true' else False,
# #                     other_activities = i['Other Activities'],
# #                     kuks = True if i['Kuks'].upper()=='true' else False,
# #                     quaas = True if i['Quaas'].upper()=='true' else False,
# #                     moans = True if i['Moans'].upper()=='true' else False,
# #                     tail_flags = True if i['Tail flags'].upper()=='true' else False,
# #                     tail_twitches = True if i['Tail twitches'].upper()=='true' else False,
# #                     approaches = True if i['Approaches'].upper()=='true' else False,
# #                     indifferent = True if i['Indifferent'].upper()=='true' else False,
# #                     runs_from = True if i['Runs from'].upper()=='true' else False,
# #                     )
# #                 if created:
# #                     s.save()
# #                     # print(f'Squirrel {unique_squirrel_id} has been loaded.')
# #                 else:
# #                     raise ValueError('Wrong import data')
