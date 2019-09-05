import dj_database_url
from .base import *
from . import get_env_variable


SOCIAL_AUTH_EVENTBRITE_KEY = get_env_variable('SOCIAL_AUTH_EVENTBRITE_KEY')
SOCIAL_AUTH_EVENTBRITE_SECRET = get_env_variable(
            'SOCIAL_AUTH_EVENTBRITE_SECRET',
            )

SECRET_KEY = get_env_variable('SECRET_KEY')
ALLOWED_HOSTS = ['floating-ocean-20992.herokuapp.com']

DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'todolist',
                'USER': 'name',
                'PASSWORD': '',
                'PORT': '',
            }
        }

DB_FROM_ENV = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(DB_FROM_ENV)
