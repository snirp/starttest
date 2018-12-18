# Django starter templates with a choice of authentication
This is a collection of mildly opinionated Django starter templates. The main goal is to get started quickly in common cases and avoid repetition or bad practices during setup. With this I am able to address some personal gripes. Not everyone may share these and it's open to discussion what exeactly represents "best practice". You can check out different branches 

## Installed libraries:

+ django-debug-toolbar - [docs](https://django-debug-toolbar.readthedocs.io)
+ django-extensions - [docs](https://django-extensions.readthedocs.io)
+ psycopg2 - [docs](http://initd.org/psycopg/docs/)
+ django-allauth - [docs](https://django-allauth.readthedocs.io)
+ django-email-bandit - [docs](https://django-email-bandit.readthedocs.io/en/latest/)

## Configuration choices

+ Stick to the default Django folder layout, with the name of the project and the project-folder simply: `project`
+ Manage confidentional and environment-spefic settings in a `.env` file (environmental variables)
+ A `base` settings file is extended with phase-specific settings files (`development`, `production`, etc)
+ The debug-toolbar will only be activated when `DEBUG` is set to `True`
+ Postgres is the default database engine

## Features

+ A basic custom user model `users.models.User` that inherits from `AbstractBaseUser`
+ Easy choice between `username`, `email` or `username_email` authentication methods
+ Fully compatible with `allauth` views and templates for account management
+ Emails sent in the development phase are intercepted and sent to an address you choose

# Get started

## Checkout authentication method
```
git init
git remote add django-starters git://github.com/snirp/django2.1-starters.git
git checkout -b master django-starters/<branchname>
pipenv install
```
You can checkout one of the following branches, each representing a different authentication method:
+ `username` **Authenticate with username**: password has to be entered twice; email address is not required.
+ `email` **Authenticate with email address**: users have no username, the email will serve as the username field
+ `username_email` **Authenticate with email or username**: both username and email are required
+ `master` **Switch between methods**: choose one the above methods by setting the corresponding value as `ACCOUNT_AUTHENTICATION_METHOD` in `settings/base.py` (default is `username`).

In the `master` branch `users/models.py` and `users/admin.py` contain a few `if ... else` statements that make sure the model and the admin pages match the authentication choice. This allows you to quickly switch between methods, which can be useful if you are trying decide on the proper authentication method. Otherwise it might be easier to start with one of the other branches.

## Create database

Replace the values of `my_database`, `my_user`, and `my_password` with your own values. 
```
psql
postgres=# CREATE DATABASE my_database;
postgres=# CREATE USER my_user WITH ENCRYPTED PASSWORD 'my_password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE my_database TO my_user;
postgres=# \q
```

## Set environment variables

The triple dotted `...env` file holds a template for your environmental settings. Proceed as follows:

1. Double check that `.gitignore` has a line with `.env`, so git will not track the (confidential) environment settings.
1. Rename from ...env to .env (`mv ...env .env`)
1. Edit passwords, secret keys and environment-specific settings to suit your environment. The database settings should match the values of the Postgres database you created.


## Edit settings, apply migrations and get started

Configure `BANDIT_EMAIL` in `project/settings/development.py` to match your email address to use during development.

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

You can edit the Site settings in the admin to match your project.

# What's next?
With Allauth, adding OAuth authentication by third party providers is a breeze. Check out their docs to get started.

Other recommended libraries:
+ Django REST Framework
+ ...
