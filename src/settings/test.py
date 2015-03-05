# coding: utf-8
from common import *
import os

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS'  : { 'init_command' : 'SET storage_engine=MyISAM', },
    }
}

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS += (
    "django_nose",
    "coverage",
)

###CONFIGURE TEST
# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on ussd apps
NOSE_ARGS = [
    # '--with-coverage',
    '--verbosity=0',
    '--debug-log=test_log.txt',
    # '--cover-package= a-app',
]
