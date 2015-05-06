from production import *

#settings specific to heroku platform
#from memcacheify import memcacheify
from postgresify import postgresify

########## DATABASE CONFIGURATION
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
#CACHES = memcacheify()
########## END CACHE CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.herokuapp.com']
########## END ALLOWED HOST CONFIGURATION
