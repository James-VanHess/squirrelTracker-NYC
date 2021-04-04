import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.forms import ModelForm



class Squirrel(models.Model):
    '''
    Creates a new sighting incident for the squirrelTracker app
    '''
    
    #                                                               #
    ## fields for information needed, going down the required list ##
    #                                                               #   


    # Lattitude 
    x = models.FloatField(blank=False,)
    
    # Longitude
    y = models.FloatField(blank=False,)

    # Lat/Long
    lat_long = f'Point ({x}, {y})'


    # Unique Squirrel ID
    unique_squirrel_id = models.CharField(
        max_length=100, 
        primary_key=True,
        default=None,
        blank=False
        )

    # Shift
    am = 'AM'
    pm = 'PM'
    shift_choices = ((am, 'AM'), (pm, 'PM'),)
    
    shift = models.CharField(
        max_length=100,
        choices=shift_choices, 
        blank=True,
        )
    
    # Date
    date = models.DateField(
        max_length=100, 
        blank=True,
        )
    
    # Age
    adult = 'Adult'
    juvenile = 'Juvenile'
    age_choices = ((juvenile, 'Juvenile'), (adult, 'Adult'))
   
    age = models.CharField(
        max_length=100, 
        choices=age_choices,
        blank=True,
        null=True,
        )

    # Primary Fur Color
    gray = 'Gray'
    cinnamon = 'Cinnamon'
    black = 'Black'
    color_choices = (
        (gray, 'Gray'), 
        (cinnamon, 'Cinnamon'), 
        (black, 'Black'),
        )

    primary_fur_color = models.CharField(
        max_length=100,
        choices=color_choices,
        blank=True,
        null=True,
    )
    
    # Location
    ground_plane = 'Ground Plane'
    above_ground = 'Above Ground'
    location_choices = (
        (ground_plane, 'Ground Plane'),
        (above_ground, 'Above Ground'),
    )
    location = models.CharField(
        max_length=100,
        choices=location_choices,
        blank=True,
        null=True,
    )
    # Specific Location
    specific_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    # Running
    running = models.BooleanField(blank=True)

    # Chasing
    chasing = models.BooleanField(blank=True)

    # Climbing
    climbing = models.BooleanField(blank=True)

    # Eating
    eating = models.BooleanField(blank=True)

    # Foraging
    foraging = models.BooleanField(blank=True)

    # Other Activities
    other_activities = models.BooleanField(blank=True)

    # Kuks
    kuks = models.BooleanField(blank=True)

    # Quaas
    quaas = models.BooleanField(blank=True)

    # Moans
    moans = models.BooleanField(blank=True)

    # Tail flags
    tail_flags = models.BooleanField(blank=True)

    # Tail twitches
    tail_twitches = models.BooleanField(blank=True)

    # Approaches
    approaches = models.BooleanField(blank=True)

    # Indifferent
    indifferent = models.BooleanField(blank=True)

    # Runs from
    runs_from = models.BooleanField(blank=True)

    #                                                               #
    ## end -fields for information needed from required list+      ##
    #                                                               #   


    # traditional Class module to return a readable string of information
    def __str__(self):
        return self.unique_squirrel_id

    
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
