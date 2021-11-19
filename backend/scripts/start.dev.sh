#!/bin/bash

echo $ls
python3 app/manage.py migrate
python3 app/manage.py collectstatic --no-input
python3 app/manage.py runserver 0.0.0.0:8000