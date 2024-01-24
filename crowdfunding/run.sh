#!/usr/bin/env bash
python manage.py migrate
python manage.py createsuperuser --noinput
gunicorn --bind :8000 --workers 1 crowdfunding.wsgi


