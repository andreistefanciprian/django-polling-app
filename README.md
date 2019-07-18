# Description

Django tutorial at:
https://docs.djangoproject.com/en/2.2/intro/tutorial01/

# Django steps to build this project 

```buildoutcfg
# create virtual env
virtualenv -p /usr/local/bin/python3 django-polling-app

# Activate env
source django-polling-app/bin/activate

# Install requirements
pip install -r requirements.txt

# Create db schema
python manage.py makemigrations polls

# Create db tables
python manage.py migrate

# Start Django development server
python manage.py runserver 0:8080

```

# Django commands
```buildoutcfg

# Create project
django-admin startproject mysite

# Create polling app, polls
python manage.py startapp polls

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

# API play
```buildoutcfg
python manage.py shell

from polls.models import Choice, Question
from django.utils import timezone

# displays all the questions in the database.
Question.objects.all()

# Create a new Question
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

# Display ID.
q.id

# Access model field values via Python attributes.
q.question_text
q.pub_date

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# Filters
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

# Get the question that was published this year.
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# Lookup by a primary key
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
q.was_published_recently()

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
c.question

# Display any choices from the related object set
q.choice_set.all()
q.choice_set.count()

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)

# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```