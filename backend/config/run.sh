#!/bin/sh
python manage.py migrate
gunicorn 'backend.wsgi' -b 0.0.0.0:80 --access-logfile - --log-level info