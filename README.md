# Description

Django tutorial at:
https://docs.djangoproject.com/en/2.2/intro/tutorial01/

# Django steps to build this project 

```bash
# create virtual env
virtualenv -p /usr/local/bin/python3 django-polling-app

# Activate env
source django-polling-app/bin/activate

# Install requirements
pip install -r requirements.txt

# Create project
django-admin startproject mysite

# Start Django development server
python manage.py runserver 0:8080

# Create polling app, polls
python manage.py startapp polls

# Create db tables
python manage.py migrate

# Create db schema
python manage.py makemigrations polls

# The sqlmigrate command takes migration names and returns their SQL
python manage.py sqlmigrate polls 0001

# Checks for any problems in your project without making migrations or touching the database
python manage.py check

# takes all the migrations that haven’t been applied 
# (Django tracks which ones are applied using a special table in your database called django_migrations) 
# and runs them against your database
# essentially, synchronizing the changes you made to your models with the schema in the database.
python manage.py migrate

```