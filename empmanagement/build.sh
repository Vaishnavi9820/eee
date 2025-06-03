#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create necessary directories
mkdir -p static
mkdir -p staticfiles

# Copy static files from empmanagement/static to static/
if [ -d "empmanagement/static" ]; then
    cp -r empmanagement/static/* static/
fi

# Install whitenoise
pip install whitenoise

# Set debug to false for collectstatic
sed -i "s/DEBUG = True/DEBUG = False/g" empmanagement/settings.py

# Collect static files
python manage.py collectstatic --noinput --clear

# Set debug back to true
sed -i "s/DEBUG = False/DEBUG = True/g" empmanagement/settings.py
