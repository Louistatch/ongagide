"""
WSGI config for agide project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import dotenv
from django.core.wsgi import get_wsgi_application

# Charger les variables d'environnement depuis .env
dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agide.settings')

application = get_wsgi_application()
