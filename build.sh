#!/usr/bin/env bash
# build.sh
# Exit the script immediately if any command fails
set -o errexit  

# Install all required packages
pip install -r requirements.txt

# Collect static files (CSS, JS, images) for Django
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
