#!/usr/bin/env bash
# Exit on error and print commands as they are executed
set -o errexit -o xtrace

echo "=== Starting build process ==="

# Install Python dependencies
echo "\n=== Installing Python dependencies ==="
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations
echo "\n=== Running database migrations ==="
python manage.py migrate --noinput

# Collect static files
echo "\n=== Collecting static files ==="
python manage.py collectstatic --noinput --clear
echo "\n=== Static files collected successfully ==="

echo "\n=== Build completed successfully ==="

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
