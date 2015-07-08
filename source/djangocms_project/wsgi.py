"""
WSGI config for pyjade_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os


from django.core.handlers.wsgi import WSGIHandler
import django


class WSGIEnvironment(WSGIHandler):

    def __call__(self, environ, start_response):

        os.environ['DATABASE_URL'] = environ['DATABASE_URL']
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", environ['DJANGO_SETTINGS_MODULE'])
        django.setup()
        return super(WSGIEnvironment, self).__call__(environ, start_response)

application = WSGIEnvironment()
