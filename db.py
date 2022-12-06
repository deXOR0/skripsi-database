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


def connect_to_db():
    settings.configure(**conf)
    apps.populate(settings.INSTALLED_APPS)


if __name__ == '__main__':

    connect_to_db()

    from models import *

    disctricts = District.objects.filter(city__city_name='Jakarta Pusat')

    print([d.district_name for d in disctricts])
    print(disctricts[0].city.city_name)

    print(Pollutant.objects.filter(district__city__city_name='Jakarta Timur'))
