#!/bin/bash

# Pull latest changes from GitHub
git pull origin main

# Install/Update Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Restart Gunicorn
#sudo systemctl restart gunicorn.service
python manage.py runserver 0.0.0.0:8000

