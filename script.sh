#!/bin/bash

export DJANGO_SETTINGS_MODULE="mysite.settings.base_env"

echo "migrate"
python manage.py migrate

echo "runserver"
python manage.py runserver 0.0.0.0:8000