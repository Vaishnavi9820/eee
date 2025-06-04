"""
WSGI config for empmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

# This application object is used by the development server and any WSGI server
application = get_wsgi_application()

# Wrap the Django application with WhiteNoise for serving static files in production
application = WhiteNoise(
    application,
    root=os.path.join(Path(__file__).resolve().parent.parent, 'staticfiles'),
    prefix='/static/'
)

# Add additional directories to the WhiteNoise application
application.add_files(os.path.join(Path(__file__).resolve().parent.parent, 'static'), prefix='static/')

# Serve admin static files
admin_static = os.path.join(Path(__file__).resolve().parent.parent, 'venv', 'Lib', 'site-packages', 'django', 'contrib', 'admin', 'static')
if os.path.exists(admin_static):
    application.add_files(admin_static, prefix='admin/')


# # SAFE SUPERUSER CREATION LOGIC
# if os.environ.get('CREATE_SUPERUSER') == 'True':
#     try:
#         from django.contrib.auth import get_user_model
#         User = get_user_model()
#         if not User.objects.filter(username='admin').exists():
#             print("Creating default superuser...")
#             User.objects.create_superuser('Puushkar_Dhharaap', 'vaishnavichandgude0411@gmail.com', 'Puushkar@#987')
#     except Exception as e:
#         print("Superuser creation failed:", e)



# 🛡️ Safe superuser creation logic
if os.environ.get('CREATE_SUPERUSER') == 'True':
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            print("Creating superuser 'admin'...")
            User.objects.create_superuser('Puushkar_Dhharaap', 'vaishnavichandgude0411@gmail.com', 'Puushkar@#987')
        else:
            print("Superuser already exists.")
    except Exception as e:
        print("Superuser creation error:", e)
