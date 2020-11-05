"""
Django settings for project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from os import environ as os_environ

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1


INTERNAL_IPS = [
    '127.0.0.1',
    '172.105.91.130',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',

    'django_extensions',
    'translation_manager',
    'modeltranslation',
    'sitetree',
    'debug_toolbar',
    'tinymce',
    'photologue',
    'sortedm2m',
    'taggit',

    'pykapela.base',
    'pykapela.menu',
    'pykapela.photologue_custom',
    'pykapela.preferences',
    'pykapela.app',
    'pykapela.social',
    'pykapela.events',
    'pykapela.pages',
    'pykapela.files',
    'pykapela.gallery',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # should be called as soon as possible
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'pykapela.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'pykapela/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pykapela.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', _('English')),
    ('cs', _('Cesky')),
]

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# translation manager:
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TRANSLATIONS_BASE_DIR = os.path.join(BASE_DIR, '')

TRANSLATIONS_PROJECT_BASE_DIR = BASE_DIR

PHOTOLOGUE_DIR = 'images'

PHOTOLOGUE_GALLERY_LATEST_LIMIT = 6

#PHOTOLOGUE_PATH = os.path.join(BASE_DIR, 'media')

CACHE_VIEWS_DEFAULT_TIME = 60 * 60  # one hour

SITETREE_MODEL_TREE = 'menu.MenuTree'
SITETREE_MODEL_TREE_ITEM = 'menu.MenuItem'

PREPEND_WWW = True
