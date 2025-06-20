"""
WSGI config for empmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

# Get the Django WSGI application
application = get_wsgi_application()

# Apply WhiteNoise for serving static files in production
application = WhiteNoise(application)

# Add static files
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
application.add_files(STATIC_ROOT, prefix='/static/')

# Add media files if they exist
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
if os.path.exists(MEDIA_ROOT):
    application.add_files(MEDIA_ROOT, prefix='/media/')

# Comment out or remove the superuser creation code since it's causing issues
# The superuser already exists, so we don't need to create it again
"""
# Safe superuser creation logic
if os.environ.get('CREATE_SUPERUSER') == 'True':
    try:
        from django.contrib.auth import get_user_model
        from django.db import IntegrityError
        
        User = get_user_model()
        username = 'Puushkar_Dhharaap'
        email = 'vaishnavichandgude0411@gmail.com'
        
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser '{username}'...")
            User.objects.create_superuser(username, email, 'Puushkar@#987')
            print("Superuser created successfully.")
        else:
            print(f"Superuser '{username}' already exists. Skipping creation.")
            
    except IntegrityError as e:
        print(f"Superuser creation skipped (likely already exists): {e}")
    except Exception as e:
        print(f"Error during superuser creation: {e}")
"""
