"""Development settings and globals."""

import os
from os.path import join, normpath, dirname
from common import *

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = r"development+secret"
########## END SECRET CONFIGURATION

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
########## END DEBUG CONFIGURATION

########## ALLOWED HOSTS
ALLOWED_HOSTS = ['localhost']
########## END ALLOWED HOSTS


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
if 'DATABASE_URL' not in os.environ:
    db_dir = join(dirname(PROJECT_ROOT), 'database')
    os.environ['DATABASE_URL'] = 'sqlite:///' + db_dir + '/project.db'

import dj_database_url
DATABASES = {
    'default':
        dj_database_url.config()
}
########## END DATABASE CONFIGURATION
