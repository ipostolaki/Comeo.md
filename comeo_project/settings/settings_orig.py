"""
Django settings for comeo_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7g%&sc*lv@c@m8f(+ltbro-8hug&wi4p@@=s-mzzs_+=lhz3-6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comeo_app',
    'crispy_forms',
    'bootstrapform',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'comeo_project.urls'

WSGI_APPLICATION = 'comeo_project.wsgi.application'


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

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# non Default

STATIC_URL = '/home/comeo_env/comeo_project/comeo_app/static/comeo_app/'

LOGIN_URL = '/login/'

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request','comeo_app.context_processors.custom_processor')

LOGIN_REDIRECT_URL = '/profile/'

AUTH_USER_MODEL = 'comeo_app.ComeoUser'

MEDIA_ROOT = '/Users/ipostolaki/envs/comeo_sync/comeo_project/media'
MEDIA_URL = '/uploaded/'

LOCALE_PATHS = ('/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/locale/',)

LANGUAGES = (
    ('ru', _('Russian')),
    ('ro', _('Romanian')),
)

LANGUAGE_CODE = 'ru'

# Email

DEFAULT_FROM_EMAIL = 'contact@comeo.org.md'
SERVER_EMAIL = 'contact@comeo.org.md'


if DEBUG:
    DEBUG_EMAIL = True

if DEBUG_EMAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = 'email-dummy/'
else:
    # custom email backend which support ssl connection supported by zoho
    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    EMAIL_HOST = 'smtp.zoho.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = 'contact@comeo.org.md'
    EMAIL_HOST_PASSWORD = 'Definepass1'


# Debug

OUTSIDE = os.environ.get('OUTSIDE','')

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_panel.middleware.DebugPanelMiddleware',)
    INSTALLED_APPS += ('debug_toolbar','debug_panel',)

# Custom non django

CRISPY_TEMPLATE_PACK = 'bootstrap3'