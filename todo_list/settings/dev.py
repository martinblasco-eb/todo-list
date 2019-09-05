from .base import *
from .import get_env_variable


SOCIAL_AUTH_EVENTBRITE_KEY = ''
SOCIAL_AUTH_EVENTBRITE_SECRET = ''

DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
