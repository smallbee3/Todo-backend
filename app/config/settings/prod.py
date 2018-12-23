from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
    '.amazonaws.com',
    'trello-api.smallbee.me',
]

WSGI_APPLICATION = 'config.wsgi.prod.application'


import_secrets()
