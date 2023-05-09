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

Migrate the the Pending Migration
        python3 manage.py migrate




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

To migrate changes
        python3 manage.py migrate

Allows you to play with the API
        python3 manage.py shell

{% %} = confused acorn for value
{{ }} = cross hairs for logic

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
        c = Cat(name="Biscuit", breed='Sphinx', description='Evil looking cuddle monster. Hairless', age=2)
use c.__dict__ to see the entry
use c.id to give it an id
use c.save() to save it

if we're making routes to a new page:
        1. create the html page for the route (if needed)
        2. set the url path in <app name>/url.py
        3. set the route in the <app name>/views.py
        4. set the code in the html to be able to pull the data from model
        5. test
