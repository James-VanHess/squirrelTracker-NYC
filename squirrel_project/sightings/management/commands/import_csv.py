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