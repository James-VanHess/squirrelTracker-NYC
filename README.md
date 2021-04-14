squirrelTracker-NYC
==============

Project background description
---------------
This is a web application project developed with Django framework to keep track of all the known squirrels in Central Park. We used a dataset from the 2018 Central Park Squirrel Census. 

The users are allowed to import, manipulate and view squirrel data from the sightings, as well as having the ability to visualize the sightings on a map of Central Park. 


Main contributors
-----------------
### Project Group 9

UNIs: [djm2248, jfv2110]

David Jefe Margatan - djm2248

James Van Hess - jfv2110


Prerequisites
-------------
The prerequisites softwares are Python3 and Django web framework.
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com)
- [Django-Leaflet](https://django-leaflet.readthedocs.io/en/latest/)  


Main Functions
--------------
The applications provides the users with a map displaying the location of the squirrel sightings in Central Park. Beside this, the function also includes viewing, creating, and updating the squirrels' sighting data as well as viewing the general statistics of them.

Data Source
------------
We use squirrel data [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which was counted by the [**Squirrel Census**](https://www.thesquirrelcensus.com/). 

This data set contains data from 3,023 sightings, including location coordinates, age, primary and etc..


Management Commands
-------------------
**Import**: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. *If using csv in our repo, /path/to/file.csv = 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv*

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

**Export**: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

Sightings
----------
## View All Sightings
All the sightings can be viewed at the main page and the user can get access to the detailed information about each sighting through the link of unique squirrel id.

    located at: /sightings

## Create New Sightings
A new spot creation can be made by each user by clicking the "New Spot Creation" button and then users can be firected to a new page to update the information.

    located at: /sightings/add
    
    
## View Squirrel Statistics
The Squirrel Status Summary can be viewed at main page through the link below.
 
    located at: /sightings/stats


## Edit Squirrel Sighting Data
Users can update sighting information about each squirrel sighting via the link listed at main page.

    located at: /sightings/update/<unique-squirrel-id>


## View Map 
There is a map visualizing all the locations of squirrels in the Central Park.
    
    located at: /sightings/map