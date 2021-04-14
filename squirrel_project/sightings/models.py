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
    latitude = models.FloatField(blank=False, null=False)
    
    # Longitude
    longitude = models.FloatField(blank=False, null=False)

    # Lat/Long
    lat_long = f'Point ({latitude}, {longitude})'


    # Unique Squirrel ID
    unique_squirrel_id = models.CharField(
        max_length=50, 
        primary_key=True,
        )

    # Shift
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'),)
    
    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES, 
        default='Unknown',
        )
    
    # Date
    date = models.DateField( 
        blank=True,
        null=True,
        )
    
    # Age
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = ((JUVENILE, 'Juvenile'), (ADULT, 'Adult'))
   
    age = models.CharField(
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

    primary_fur_color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICES,
        default='Unknown',
    )
    
    # Location
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'
    LOCATION_CHOICES = (
        (GROUND, 'Ground Plane'),
        (ABOVE, 'Above Ground'),
    )
    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES,
        default='Unknown'
    )
    # Specific Location
    specific_location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    # Running
    running = models.BooleanField(default=False)

    # Chasing
    chasing = models.BooleanField(default=False)

    # Climbing
    climbing = models.BooleanField(default=False)

    # Eating
    eating = models.BooleanField(default=False)

    # Foraging
    foraging = models.BooleanField(default=False)

    # Other Activities
    other_activities = models.CharField(
        max_length=200, 
        blank=True,
        null=True, 
        )

    # Kuks
    kuks = models.BooleanField(default=False)

    # Quaas
    quaas = models.BooleanField(default=False)

    # Moans
    moans = models.BooleanField(default=False)

    # Tail flags
    tail_flags = models.BooleanField(default=False)

    # Tail twitches
    tail_twitches = models.BooleanField(default=False)

    # Approaches
    approaches = models.BooleanField(default=False)

    # Indifferent
    indifferent = models.BooleanField(default=False)

    # Runs from
    runs_from = models.BooleanField(default=False)

    #                                                               #
    ## end -fields for information needed from required list+      ##
    #                                                               #   