# -*- coding: utf-8 -*-
import os

PATH = os.path.realpath(os.path.dirname(__file__))

## local (and default) settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'emyller',
    }
}

## loading production settings

from socket import gethostname

IN_PRODUCTION = gethostname() == 'localhost'

if IN_PRODUCTION:
    from psettings import *

## other settings

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS = (
    ('Evandro Myller', 'evandromyller@gmail.com'),
)

TIME_ZONE = 'America/Fortaleza'
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(PATH, '_media')
PROJECT_ALIAS = os.path.basename(PATH)

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
LOGIN_URL = '/login/'

SITE_ID = 1
SECRET_KEY = '8u=a9%fp-3(f$cnd7jr0fq#&a2-%&ucoicy-1^n@maygql1eoo'
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = PROJECT_ALIAS + '.urls'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

## loaders

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PATH, '_templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

if DEBUG: MIDDLEWARE_CLASSES += 'debug_toolbar.middleware.DebugToolbarMiddleware',

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.comments',

    ## third-party
    'south',

    ## local apps
    'core',
)

if not IN_PRODUCTION: INSTALLED_APPS += 'debug_toolbar',
