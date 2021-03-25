#!/bin/sh
python manage.py migrate
python manage.py runserver
cd frontend/
npm run serve
gunicorn 'HUAWEI.wsgi' -b 0.0.0.0:80 --access-logfile - --log-level info