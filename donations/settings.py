"""
Django settings for donations project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]

from registration_defaults.settings import *

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    "registration_defaults",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'registration',
    'app',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'donations.urls'

WSGI_APPLICATION = 'donations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'app/templates'), REGISTRATION_TEMPLATE_DIR,)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# For Django-Registration
ACCOUNT_ACTIVATION_DAYS = 7

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'


EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('POSTMARK_SMTP_SERVER')
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.environ.get('POSTMARK_API_KEY')
EMAIL_HOST_PASSWORD = os.environ.get('POSTMARK_API_KEY')
DEFAULT_FROM_EMAIL = 'vzvenyach@dccouncil.us'

LOGIN_REDIRECT_URL = '/admin'

# API

TASTYPIE_DEFAULT_FORMATS = ['json']

# try to load local_settings.py if it exists
try:
  from local_settings import *
except Exception as e:
  pass