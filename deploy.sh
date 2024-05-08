#!/bin/bash

#Know the current user running the Script
echo "Current User running the deploy.sh =========>: $(whoami)"

# Navigate to the project directory
echo "Navigating to the Project Folder"
cd /home/projectcicd/aawscicd

# Activate the virtual environment
echo "Activating the Virtual Environment"
source ../venv/bin/activate

# Kill the Django development server if it's already running
echo "Stopping Django development server if running..."
kill $(lsof -t -i:8000)  # Kill process using port 8000 (change port if necessary)

# Pull latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull origin main

# Install/Update Python dependencies
echo "Installing/updating Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Django development server
echo "Starting Django development server..."
nohup python manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &

echo "Development Server started in the background"

sleep 10

echo "The Development Server is up and running"

