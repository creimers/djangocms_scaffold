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

