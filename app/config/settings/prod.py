from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
    '.amazonaws.com',
    'todo-api.smallbee.me',
]

WSGI_APPLICATION = 'config.wsgi.prod.application'


import_secrets()
