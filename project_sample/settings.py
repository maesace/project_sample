"""
Django settings for project_sample project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, 'project_sample')
SHARED_DIR = environ.Path(__file__) - 3


#env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
#env_file = str(os.path.join(BASE_DIR, '.env'))
#env.read_env(env_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b1pncm6&@yg1p+3lxgso&pbvnzecvx(c#5*_-r52s=4zgtya5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

LOCAL_APPS = (
    'project_sample.accounts',
    'project_sample.web',
)

THIRD_PARTY_APPS = (
    'materializecssform',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_sample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APPS_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "project_sample.web.context_processors.custom_context_processors",
            ],
        },
    },
]

WSGI_APPLICATION = 'project_sample.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(os.path.join(APPS_DIR, 'web/static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = str(SHARED_DIR('shared/media'))
STATIC_ROOT = str(SHARED_DIR('shared/static'))

# Custom User model
AUTH_USER_MODEL = 'accounts.User'


# Logging
def levelname_filter(*args):
    class LevelNameFilter(logging.Filter):
        def filter(self, record):
            return record.levelname.lower() in args
    return LevelNameFilter


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'debug_only': {
            '()': levelname_filter('debug'),
        },
        'info_only': {
            '()': levelname_filter('info'),
        },
        'warn_only': {
            '()': levelname_filter('warning'),
        },
        'error_only': {
            '()': levelname_filter('error', 'critical'),
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'sitelog.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'debug.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'info.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warn_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'warning.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'error.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['warning', 'error', 'default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'default': {
            'handlers': ['console', 'default', 'debug', 'info'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# Website config
SITE_NAME = 'Sample site'

# menu label : menu url name
MENU_ITEMS = [
]

LOGIN_REDIRECT_URL = 'user-view'
LOGOUT_REDIRECT_URL = 'user-view'
