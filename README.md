# Hall One Jamband a.k.a Universe Website Project
Originally prototyped and developed at https://github.com/TZBAvyy/JamBandWebApp

## Setup
### Quickstart
1. Create and activate a python venv
2. `pip install -r requirements.txt`
3. `python website/manage.py runserver`

### Additional
- Create .env file with:

        DEFAULTUSERNAME = ...
        DEFAULTUSERPASS = ...
        SUPERUSERNAME = ...
        SUPERUSERPASS = ...
        DEBUG = ...
        SECRET_KEY = ...

## Project Overview

### Home
Features upcoming events and practices  
TODO: Add photos and features of past events   
TODO: Add contact us form and info

### Schedule
Showcases practice schedule for bands in weekly calendar format  
Allows for creation, deletion and update of practices

### TBC

## Project Dependacies

    # Python
    Python == 3.10.12
    Django == 5.1.4
    django-extensions == 3.2.3
    django-widget-tweaks == 1.5.0
    python-decouple == 3.8

    # Javascript
    FullCalendar == 6.1.15

