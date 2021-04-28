#!/bin/sh
python manage.py migrate
python manage.py loadtestdata
python manage.py qcluster
gunicorn 'backend.wsgi' -b 0.0.0.0:80 --access-logfile - --log-level info