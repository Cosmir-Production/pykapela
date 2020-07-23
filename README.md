# README #

This app is primary for music bands. It aims to offer almost everything what you need on a website for your band. Also some thinks are tweaked as bands can appriciate.

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

Need website for you music band?

Try this tool, which brings all basic pages and modules targeting your audience and promoters.

You may have basic knowledge of python and programming, but maybe you can manage without it.
What you may need is knowledge of HTML and CSS

* Recommended is latest master version for now.

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Features ###
* It's free and will be forever - do what you need with no commercials
* Events - events are smart way module to promote your concerts
* Social network module will connect your website with these

### Requirements ###
* python3
* postgres or other database

### Installation ###

get in working directory

`cd <yourworkingdirectory>`

create enviroment (server):

`cd ..`

`python3 -m venv yourproject`

`cd yourproject; source bin/activate`

create environment (local):

`mkvirtualenv --python=/usr/bin/python3 <yourwebsitename>`

`workon <yourwebsitename>`

make sure to have correct rights:

`sudo chmod 774 -R /srv/yourproject`

`sudo chown www-data:www-data -R /srv/yourproject`

clone the code!

`git clone git@bitbucket.org:Cosmir-Production/pykapela.git .`

create PostgreSQL database:

`create database myproject;`

`create user youruser with password 'yourcustompassword'`

`grant all privileges on database youruser to myproject;`

create and update database settings:

`cp pykapela/settings/database.default.py project/settings/database.py`

create and update local settings:

`cp pykapela/settings/settings_local.default.py project/settings/settings_local.py`

install dependencies:

`pip3 install -r requirements/production.txt`

run database migrations:

`./manage.py makemigrations`

run local server:

`./manage.py runserver`

run these to seed the database:

`./manage.py collectstatic`

`./manage.py sitetreeload --mode=replace treedump.json`

Type this in your browser

`http://127.0.0.1:8000/`

Celebrate ;-)

### Contribution guidelines ###

* Writing tests, haha
* Code review, maybe
* Other guidelines, we'll see
