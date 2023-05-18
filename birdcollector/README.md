project name - birdcollector
db - birdcollector

Getting started in Django. From terminal.
    1. Turning a folder into a Django environment:
            python3 -m venv django_env
    2. Installing Django
            python3 -m pip install Django
    3. Upgrading Django
            python3.11 -m pip install --upgrade pip

To activate a django environment in order to start a project
        source django_env/bin/activate

To start project
        django-admin startproject <projectname>
        * go ahead and cd into it
        * make sure you are in the project but not too deep in. ls to check

Establish project framework
        python3 manage.py startapp main_app

Add this to settings.py in project
        INSTALLED_APPS = [
	'main_app',
        ]

*run server to check everything is operating. check localhost:8000

Connect to project database:
        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '<projectname>',
                }
        }

Make migration files for a DB after its been created
        python3 manage.py makemigrations
How to show whats been migrated
        python3 manage.py showmigration
Migrate the the Pending Migration
        python3 manage.py migrate

django to git thought
makemigrations ==> add/commit
migrate ==> push


https://github.com/takis-fuego-cohort/lessons-and-labs/blob/main/Unit_3/3-django/3.1-intro-django.md
https://docs.djangoproject.com/en/4.2/intro/tutorial01/
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
https://docs.djangoproject.com/en/4.2/intro/tutorial03/
https://docs.djangoproject.com/en/4.2/intro/tutorial04/

***DO API Section

To run the app
        python3 manage.py runserver

Creates an app (polls)
        python3 manage.py startapp polls


Allows you to play with the API
        python3 manage.py shell

{% %} = confused acorn for logic
{{ }} = cross hairs for values

when updating a database, we need to make migrations, then do the migrations.
        python3 manage.py makemigrations
        - to check migrations, run this
        python3 manage.py showmigrations
        - once you're ready to migrate, run this
        python3 manage.py migrate
If you need to make adjustments to the model, delete the migrations first before modifying the model. you'll run into issues if you dont.
think of makemigrations/migrate like addcommit/push

When putting in data for the model, look at Step 7 of here: https://github.com/takis-fuego-cohort/lessons-and-labs/blob/main/Unit_3/3-django/3.3-django-models.md

## Creating Data using a shell
from terminal, use
        python3 manage.py shell
then use
        from main_app.models import <db name>
        - if you ever leave the shell and the db, you will need to import each time.
then
        <dbname>.objects.all()
                it will bring up <QuerySet []>
here is an example of data entry
        b = Bird(name="Tweetie", breed='canary', description='innocent yellow birdie', age=2)
        keep in mind that this is really just a reflection of the information you put in the model.
        using this is good for putting dummy data for a model. you can put data in the views, but eventually you'll need a better database management system. this would be the next step.
use <database letter> b.__dict__ to see the entry 
use b.id to give it an id
use b.save() to save it
# there is a lot you can do in finding your data. look up <db name>.objects.<filter mod> to find more info.
make sure when you're done, you import it in the <main_app>/views.py

# creating an admin
Follow the prompts and have a nice day
        python3 manage.py createsuperuser
        python3 manage.py changepassword <user_name>
Don't forget to register your models on the admin site.
        admin.site.register(<database name)

Step 10 of django-models has solid advice for coding CRUD

when applying a new feature (like a new CRUD), here is the process that makes sense to you.
        - if CRUD needs a specific HTML, create that HTML for it.
        - create the path() in <main_app>/url.py
        - create the def (if function based) or class (if classed based) route in <main_app>/views.py
        - test code by accessing route directly in html.
        - on success of accessing route, go back to HTML and properly connect links for functionality.

Be keen on working the the main_app/url and main_app/views. these need to be aligned properly in order to call the html. you can create the html first and for testing, but without proper routes, server will crash.


useful sql commands
psql - runs sql shell

help -- general help
\?   -- help with psql commands
\h   -- help with SQL commands
\l   -- Lists all databases
\c   -- Connect to a database
\d   -- List tables in database
\q   -- exits psql
q    -- exits a psql list or dialogue

start on 3.5, complete to 3.6
finish SQL HW