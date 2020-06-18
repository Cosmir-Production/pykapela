
import os

BASE_LOG_DIR = '/tmp'

DEBUG_LOG_FILENAME = 'django-project.log'
DEBUG_LOG_FILE = os.path.join(BASE_LOG_DIR, DEBUG_LOG_FILENAME)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d <%(name)s|%(filename)s:%(lineno)s> %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': DEBUG_LOG_FILE,
            'interval': 1,
            'when': 'D',
            'backupCount': 90,
            'formatter': 'verbose',

        },
    },
    'loggers': {
        '*': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
