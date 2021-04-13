import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse
from django.forms import ModelForm



class Meta:
    managed = True

class Squirrel(models.Model):
    '''
    Creates a new sighting incident for the squirrelTracker app
    '''
    # traditional Class module to return a readable string of information
    def __str__(self):
        return self.unique_squirrel_id 

    #                                                               #
    ## fields for information needed, going down the required list ##
    #                                                               #   


    # Lattitude 
    LATITUDE = models.FloatField(blank=False, null=False)
    
    # Longitude
    LONGITUDE = models.FloatField(blank=False, null=False)

    # Lat/Long
    lat_long = f'Point ({LATITUDE}, {LONGITUDE})'


    # Unique Squirrel ID
    unique_squirrel_id = models.CharField(
        max_length=50, 
        primary_key=True,
        )

    # Shift
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'),)
    
    SHIFT = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES, 
        default='Unknown',
        )
    
    # Date
    DATE = models.DateField( 
        blank=True,
        null=True,
        )
    
    # Age
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = ((JUVENILE, 'Juvenile'), (ADULT, 'Adult'))
   
    AGE = models.CharField(
        max_length=50, 
        choices=AGE_CHOICES,
        blank=True,
        null=True,
        )

    # Primary Fur Color
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    COLOR_CHOICES = (
        (GRAY, 'Gray'), 
        (CINNAMON, 'Cinnamon'), 
        (BLACK, 'Black'),
        )

    PRIMARY_FUR_COLOR = models.CharField(
        max_length=100,
        choices=COLOR_CHOICES,
        default='Unknown',
    )
    
    # Location
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'
    location_choices = (
        (GROUND, 'Ground Plane'),
        (ABOVE, 'Above Ground'),
    )
    LOCATION = models.CharField(
        max_length=50,
        choices=location_choices,
        default='Unknown'
    )
    # Specific Location
    SPECIFIC_LOCATION = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    # Running
    RUNNING = models.BooleanField(default=False)

    # Chasing
    CHASING = models.BooleanField(default=False)

    # Climbing
    CLIMBING = models.BooleanField(default=False)

    # Eating
    EATING = models.BooleanField(default=False)

    # Foraging
    FORAGING = models.BooleanField(default=False)

    # Other Activities
    OTHER_ACTIVITIES = models.CharField(
        max_length=200, 
        blank=True,
        null=True, 
        )

    # Kuks
    KUKS = models.BooleanField(default=False)

    # Quaas
    QUAAS = models.BooleanField(default=False)

    # Moans
    MOANS = models.BooleanField(default=False)

    # Tail flags
    TAIL_FLAGS = models.BooleanField(default=False)

    # Tail twitches
    TAIL_TWITCHES = models.BooleanField(default=False)

    # Approaches
    APPROACHES = models.BooleanField(default=False)

    # Indifferent
    INDIFFERENT = models.BooleanField(default=False)

    # Runs from
    RUNS_FROM = models.BooleanField(default=False)

    #                                                               #
    ## end -fields for information needed from required list+      ##
    #                                                               #   



    
# class Question(models.Model):
#     '''
#     Creates a question for the polls app
#     '''
    
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
    
#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

   
    
# class Choice(models.Model):
#     '''
#     Saves the choice from the polls app
#     '''

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text
