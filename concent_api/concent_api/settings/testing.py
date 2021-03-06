# pylint: disable=unused-wildcard-import
from middleman.constants import DEFAULT_INTERNAL_PORT
from .base import *  # NOQA  # pylint: disable=wildcard-import

SECRET_KEY = 'testkey'

DEBUG = True

DATABASES = {
    # 'default' must be set for testing, otherwise tests won't work
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'test_default'
        }
    },
    'control': {
        # NAME intentionally left unset, in case tests try to access the production database.
        # This could happen e.g. if someone executes a query at module level.
        'ENGINE':          'django.db.backends.postgresql_psycopg2',
        'USER':            'postgres',
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'test_control'
        }
    },
    'storage': {
        # NAME intentionally left unset, in case tests try to access the production database.
        # This could happen e.g. if someone executes a query at module level.
        'ENGINE':          'django.db.backends.postgresql_psycopg2',
        'USER':            'postgres',
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'test_storage'
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null_handler': {'class': 'logging.NullHandler'}
    },
    'loggers': {
        '': {'handlers': ['null_handler']}
    }
}

CONCENT_FEATURES = [
    "admin-panel",
    "concent-api",
    "concent-worker",
    "conductor-urls",
    "conductor-worker",
    "gatekeeper",
    "middleman",
    "verifier",
]

STORAGE_CLUSTER_ADDRESS = 'http://localhost/'

STORAGE_SERVER_INTERNAL_ADDRESS = 'http://localhost/'

VERIFIER_STORAGE_PATH = '/tmp/'

CONCENT_MESSAGING_TIME    = 2

FORCE_ACCEPTANCE_TIME     = 5

MINIMUM_UPLOAD_RATE       = int(384 / 8)  # KB/s = kbps / 8

DOWNLOAD_LEADIN_TIME      = 3

SUBTASK_VERIFICATION_TIME = 5

CUSTOM_PROTOCOL_TIMES = True

MIDDLEMAN_ADDRESS = '127.0.0.1'

MIDDLEMAN_PORT = DEFAULT_INTERNAL_PORT

SIGNING_SERVICE_PUBLIC_KEY = b'\x19\xaew&P>\xce\xd7D\xfb\xbff)55\xc1%\xea\xebN\x0e\x05>\xf7v\x0c\x94I\xe4\xa3\x80\x1dl\xed\xb5j\xe9apZ\x8c\x86\xe2\xb2x^M}>8c\x90\x0e\xa2\xf4\x8cOb\xb1\x1er\x11\xd7\xee'

ADDITIONAL_VERIFICATION_COST = 0

# disable HandleServerErrorMiddleware in tests
if MIDDLEWARE.index('concent_api.middleware.HandleServerErrorMiddleware') is not None:
    MIDDLEWARE.remove('concent_api.middleware.HandleServerErrorMiddleware')
