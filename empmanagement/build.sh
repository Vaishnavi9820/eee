#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install system dependencies if needed
# Uncomment if you need to install system packages
# apt-get update && apt-get install -y \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# Run database migrations
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create necessary directories
echo "Creating directories..."
mkdir -p /var/www/staticfiles
mkdir -p /var/www/media

# Create local static directories
mkdir -p static
mkdir -p staticfiles

# Set permissions
echo "Setting permissions..."
chmod -R 755 /var/www/staticfiles
chmod -R 755 /var/www/media
chmod -R 755 static
chmod -R 755 staticfiles

echo "Build process completed successfully."

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
