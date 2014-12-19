# Introduction

Django Foundation is an enhanced project template for any Django application. This is a fork of out dated [django-skel](https://github.com/rdegges/django-skel).

# Installation
It requires Python 2.7 as some of the packages bundled with it do not support Python 3 namely 'django-storages'.
##Create a project directory

    $ mkdir <project_name> && cd <project_name>

##Create and start a virtualenv

    $ virtualenv <env_name>
    $ source <env_name>/bin/activate

##Intall Django and create project

    $ pip install django
    $ django-admin startproject --template=https://github.com/ludbek/django-foundation/archive/master.zip <project_name> .

##Ignore virtualenv directory
    $ echo "<env_name>" >> .gitignore # ignore virutalenv directory
##Install dependencies for development
    $ pip install -r reqs/dev.txt
##Migrate application
    $ python src/manage.py makemigrations
    $ python src/manage.py migrate
## Start application
    $ python src/manage.py runserver
## Initial deploy at Heroku
When deploying to Heroku for the first time. Following command will create specified app, add addons and environment variables.
 

    $ sudo apt-get install fabric
    $ fab bootstrap:<heroku_app_name>

## Deploy updates
To update application issue following command. Check out the `fabfile.py` for more available commands.
    $ fab deploy

# Features
In addition to the excellent features inherited from `django-skel`, it has following additional features:

- support for Django 1.7
- folder level storage at S3 with [django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage)
- host specific requirements and setting
- updated addons for heroku
- intuitive project structure

   
````
     /
        ..fabfile.py
        ..requirements.txt   
        ..docs/
        ..reqs/
        ....common.txt
        ....dev.txt
        ....prod.txt
        ....host_name.txt
        ..src/
        ....manage.py
        ....urls.py
        ....wsgi.py
        ....apps/
        ....libs/
        ....media/
        ....settings/
        ......common.py
        ......dev.py
        ......prod.py
        ......host_name.py # host specific settings
        ....static/
        ....templates
        ````
      
