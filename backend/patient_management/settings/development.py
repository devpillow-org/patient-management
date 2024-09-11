from decouple import config as env
from patient_management.settings.base import *  # noqa

#####################################################################
#                      SECURITY/DEPLOYMENT                          #
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/ #
#####################################################################
SECRET_KEY = env("SECRET_KEY", default=False, cast=str)
DEBUG = env("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["*"]


#####################################################################
#                          DATABASE                                 #
#  https://docs.djangoproject.com/en/5.0/ref/settings/#databases    #
#####################################################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME", cast=str),
        "USER": env("DATABASE_USER", cast=str),
        "PASSWORD": env("DATABASE_PASSWORD", cast=str),
        "HOST": env("DATABASE_HOST", cast=str),
        "PORT": env("DATABASE_PORT", cast=str),
    }
}
