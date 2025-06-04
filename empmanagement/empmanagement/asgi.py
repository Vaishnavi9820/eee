"""
ASGI config for empmanagement project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

# This application object is used by the ASGI server
application = get_asgi_application()

# In production, you might want to add ASGI middleware here if needed
# For example, for channels or other ASGI applications
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import re_path
# from yourapp import consumers

# application = ProtocolTypeRouter({
#     "http": application,
#     "websocket": URLRouter([
#         re_path(r"ws/some_path/$", consumers.YourConsumer.as_asgi()),
#     ]),
# })
