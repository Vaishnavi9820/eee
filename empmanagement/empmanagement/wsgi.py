"""
WSGI config for empmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

application = get_wsgi_application()


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
