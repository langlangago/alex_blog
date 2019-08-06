#!/bin/sh
source venv/bin/activate
flask db upgrade
exec gunicorn --reload -b :5000 --access-logfile - --error-logfile - manager:app 
