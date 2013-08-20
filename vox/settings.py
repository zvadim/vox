# -*- coding: utf-8 -*-
import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), "..")
project_dir = lambda p: os.path.join(PROJECT_DIR, p)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vadim Zabiiaka', 'v.zabiiaka@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.vox.li.madprogrammer.net', '.voxlegum.com']

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'uk'

gettext = lambda s: s
LANGUAGES = (
    ('uk', gettext('Uk')),
    ('ru', gettext('Ru')),
    ('en', gettext('En')),
)
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uk',)



SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
SOLID_I18N_USE_REDIRECTS = False

MEDIA_ROOT = project_dir('media')
MEDIA_URL = '/media/'

STATIC_ROOT = project_dir('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    project_dir('vox/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#rtme382a9z6o*q$l4&n13(7c5o3*5g*!+b@knn&%u@lm%0ee('


MIDDLEWARE_CLASSES = (
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'vox.urls'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    project_dir('vox/templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'sorl.thumbnail',
    'advanced_imagefield',
    'haystack',
    'modeltranslation',
    'apps.news',
    'apps.team',
    'apps.site',
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': project_dir('whoosh_index'),
    },
}


try:
    from tinymce_settings import *
except ImportError as ie:
    pass

try:
    from local_settings import *
except ImportError as ie:
    pass