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

# Collect static files
python manage.py collectstatic --no-input --clear
