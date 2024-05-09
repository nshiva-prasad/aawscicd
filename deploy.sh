#!/bin/bash

#Know the current user running the Script
echo "Current User running the deploy.sh =========>: $(whoami)"

# Navigate to the project directory
echo "Navigating to the Project Folder"
cd /home/projectcicd/aawscicd

# Activate the virtual environment
echo "Activating the Virtual Environment"
source ../venv/bin/activate

# Pull latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull origin main

# Install/Update Python dependencies
echo "Installing/updating Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting the Nginx"
sudo systemctl restart nginx

echo "Checking the Gunicorn log permissions"
sudo chown -R ubuntu:www-data /home/projectcicd/aawscicd/logs/

echo "Restarting the gunicorn.socket"
sudo systemctl restart gunicorn.socket

echo "Sleeping for 2 seconds"
sleep 2

echo "Restarting the gunicorn.service"
sudo systemctl restart gunicorn.service

echo "Sleeping for 5 seconds"
sleep 5

echo "Restarting the celery.service"
sudo systemctl restart celery.service

echo "Sleeping for 5 seconds"
sleep 5

echo "Restarting the flower.service"
sudo systemctl restart flower.service

echo "Sleeping for 2 seconds"
sleep 2

echo "Production Server started in the background"

echo "Sleeping for 1 seconds"
sleep 1

echo "The Production Server is up and running"
