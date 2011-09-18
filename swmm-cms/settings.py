DEBUG = True ## enables debug mode
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'admin@mail.net'),
)

MANAGERS = ADMINS

import os
import socket

SITE_ROOT = os.path.realpath (os.path.dirname (__file__))
SITE_NAME = 'swmm-cms'
SITE_HOST = socket.gethostname ()
SITE_ID   = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join (SITE_ROOT, 'sqlite.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join (SITE_ROOT, 'media/')
MEDIA_URL = 'http://media.%s/%s/' % (SITE_HOST, SITE_NAME)
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '+qdn5m5vwr&h_+d&2hg4nbjur*z4qb4c0loi7b^ly7i!i*$mep'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
 ## 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
 ## 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

CACHE_BACKEND = 'memcached://127.0.0.1:11211'
ROOT_URLCONF = '%s.urls' % SITE_NAME

TEMPLATE_DIRS = (
    os.path.join (SITE_ROOT, 'templates/'),
)

FIXTURE_DIRS = (
    os.path.join (SITE_ROOT, 'fixtures/'),
)

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = os.path.join (SITE_ROOT, 'session/')
SESSION_COOKIE_AGE = 28800 ## secs: 8h
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'sid.'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SECURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',

    'django.contrib.admin',
 ## 'django.contrib.admindocs',
 ## 'django.contrib.flatpages',
 ## 'django.contrib.comments',

    'attribute', 'property', 'exhib', 'about', 'forum', 'contact'
)
