# Personal-DRF-Project

# django-heroku
Minimal configuration to host a Django project at Heroku

## Create the project directory
* mkdir directory_name
* cd directory_name

## Create and activate your virtuanenv
* python -m venv venv
* **Mac/Linux:** source venv/bin/activate
* **Windows:** cd venv\Scripts
* **Windows **(if err): Set-ExecutionPolicy Unrestricted -Scope Process
* **Windows:** .\activate or .\Activate.ps1
* **Windows:** cd ../../

## Installing Django Rest Framework
* pip install djangorestframework

## Create the django project
* django-admin startproject [PROJECT_NAME]

## Creating the Git repository
* git init 
* Create a file called `.gitignore` with the following content:
```
# See the name for you IDE
.idea
# If you are using sqlite3
*.sqlite3
# Name of your virtuan env
.vEnv
*pyc
```
* git add .
* git commit -m 'Initial'

## Hidding instance configuration
* pip install python-decouple
* create an .env file at the root path and insert the following variables
- SECRET_KEY=Your$eCretKeyHere (Get this secrety key from the settings.py)
- DEBUG=True

### Settings.py
* from decouple import config
* SECRET_KEY = config('SECRET_KEY')
* DEBUG = config('DEBUG', default=False, cast=bool)

[Starter Credits](https://github.com/Gpzim98/django-heroku)
