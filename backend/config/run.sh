#!/bin/sh
python manage.py migrate
python manage.py loadtestdata
python manage.py crontab add
gunicorn 'backend.wsgi' -b 0.0.0.0:80 -w 4 --access-logfile - --log-level info --preload
