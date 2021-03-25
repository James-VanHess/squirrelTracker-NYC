# squirrelTracker-NYC
Repo for group work on developing a squirrel tracking application in Central Park, NYC


squirrelTracker-NYC
==============

Project background description
---------------
This is a web application project developped with Django framework to keep track of all the known squirrels in Central Prak. We used dataset from the 2018 Central Park Squirrel Census. The users are allowed to add, update, and view squirrel data. 


Main contributors
-----------------
### Project Group 9

UNIs: [djm2248, jfv2110]

David Jefe Margatan - djm2248

James Van Hess - jfv2110


Prerequisites
-------
The prerequisites softwares are Python3 and Django web framework.

After installing the prerequisite softwares, we are going to import the 2018 Central Park Squirrel Census dataset and then export this data to a csv file for future use.


Main Functions
------------
The applications provides the users with a map displaying the location of the squirrel sightings in Central Park. Besides, the function also includes viewing, creating, updating the squirrels' sighting data as well as viewing the general statistics of them.

### Sightings

#### View All Sightings
All the sightings can be viewed at the main page and the user can get access to the detailed information about each sighting through the link of unique squirrel id.

    located at: /sightings/

#### Create New Sightings
A new spot creation can be made by each user by clicking the "New Spot Creation" button and then users can be firected to a new page to update the information.

    located at: /sightings/new/
    
    
#### View Squirrel Statistics
The Squirrel Status Summary can be viewed at main page through the link below.
 
    located at: /sightings/stats/


#### Update Squirrel Sighting Data
Users can update sighting information about each squirrel sighting via the link listed at main page.

    located at: /sightings/<unique-squirrel-id>


### Map
There is a map visualizing all the locations of squirrels in the Central Park.
    
    located at: /map/



Deployment
------------
After the development is completed, we deploy the web application by importing Nginx, which is open source software for web serving.

We install it on our VM using the code below.
    
     sudo apt-get install nginx


The server links to the web application
--------------
#### Link to the sightings of squirrel:
#http://35.245.183.224/sightings/

#### Link to the map of squirrels:
#http://35.245.183.224/map/
