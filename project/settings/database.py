import dj_database_url

from os import environ as os_environ

if os_environ.get('PRODUCTION'):

    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'meteleska',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1'
        }
    }
