import os
from django.conf import settings
from django.apps import apps
from dotenv import load_dotenv
load_dotenv()

conf = {
    'INSTALLED_APPS': [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.sitemaps',
        'django.contrib.sites',
        'django.contrib.staticfiles',
    ],
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DATABASE_NAME'],
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'],
            'HOST': os.environ['DATABASE_HOST'],
            'PORT': os.environ['DATABASE_PORT'],
        }
    },
    'TIME_ZONE': 'Asia/Jakarta'
}

settings.configure(**conf)
apps.populate(settings.INSTALLED_APPS)

from models import *

print(City.objects.all())
print(District.objects.all())