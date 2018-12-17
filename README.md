# Django starter templates
This project contains a collection of mildly opinionated Django 2.1 starter templates. The main goal is to get started quickly in common cases and avoid repetition or bad practices during setup. With this I am able to address some personal gripes. Not everyone may share these and it's open to discussion what exeactly represents "best practice". For every template, 


```
git init
git remote add django-starters git://github.com/snirp/django2.1-starters.git
git checkout -b master django-starters/<branchname>
pipenv install
```

For all templates, the following choices have been made:
+ A pipenv virtual environment
+ The name of the project and the project-folder are simply `project` (and I rarely see reason to change that in a project, but you easily could).
+ Furthermore any changes as described under the `vanilla` branch. All other branches can be seen as inherting from vanilla (except `master`).
+ Gitignore file as included


# Branches

## [master]

The default installation of Django

## [vanilla](https://github.com/snirp/django2.1-starter/tree/vanilla)

Basic setup with a few best practices:
* Use of environment variables to manage confidential settings
* Environment-specific settings files
* Custom user model, subclassed from `AbstractBaseUser` and contained in an app called `auth`

## [email-auth](https://github.com/snirp/django2.1-starter/tree/email-auth)

