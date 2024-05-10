#!/bin/bash

# Function to echo with color
function echo_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}\e[0m"
}

# Know the current user running the script
echo_color "\e[1;35m" "Current User running the deploy.sh =======>: $(whoami)"

# Navigate to the project directory
echo_color "\e[1;36m" "Navigating to the Project Folder"
cd /home/projectcicd/aawscicd

# Activate the virtual environment
echo_color "\e[1;33m" "Activating the Virtual Environment"
source ../venv/bin/activate

# Pull latest changes from GitHub
echo_color "\e[1;34m" "Pulling latest changes from GitHub..."
git pull origin main

# Install/Update Python dependencies
echo_color "\e[1;32m" "Installing/updating Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo_color "\e[1;35m" "Collecting static files..."
python manage.py collectstatic --noinput

# Restart Nginx
echo_color "\e[1;36m" "Restarting Nginx"
sudo systemctl restart nginx

# Set log permissions
echo_color "\e[1;33m" "Checking the Gunicorn log permissions"
sudo chown -R ubuntu:www-data /home/projectcicd/aawscicd/logs/

# Restart gunicorn.socket
echo_color "\e[1;34m" "Restarting the gunicorn.socket"
sudo systemctl restart gunicorn.socket
echo_color "\e[1;34m" "Sleeping for 2 seconds"
sleep 2

# Restart gunicorn.service
echo_color "\e[1;32m" "Restarting the gunicorn.service"
sudo systemctl restart gunicorn.service
echo_color "\e[1;32m" "Sleeping for 5 seconds"
sleep 5

# Restart celery.service
echo_color "\e[1;35m" "Restarting the celery.service"
sudo systemctl restart celery.service
echo_color "\e[1;35m" "Sleeping for 5 seconds"
sleep 5

# Restart flower.service
echo_color "\e[1;36m" "Restarting the flower.service"
sudo systemctl restart flower.service
echo_color "\e[1;36m" "Sleeping for 2 seconds"
sleep 2

# Final messages
echo_color "\e[1;32m" "Production Server started in the background"
echo_color "\e[1;32m" "The Production Server is up and running"
