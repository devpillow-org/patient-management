"""
WSGI config for patient_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from decouple import config as env
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "patient_management.settings.{}".format(env("ENVIROMENT", cast=str)),
)

application = get_wsgi_application()
