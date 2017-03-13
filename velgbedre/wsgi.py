"""
WSGI config for gettingstarted project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "velgbedre.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

application = get_wsgi_application()
application = DjangoWhiteNoise(application)