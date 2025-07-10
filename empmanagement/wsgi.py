"""
WSGI config for empmanagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

try:
    logger.info("Setting up Django application...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')
    
    # Initialize Django application
    application = get_wsgi_application()
    logger.info("Django application initialized successfully")
    
except Exception as e:
    logger.error(f"Failed to initialize Django application: {str(e)}")
    logger.exception("Traceback:")
    raise
