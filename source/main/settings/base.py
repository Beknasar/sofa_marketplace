import os.path
from pathlib import Path
from .env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTION = env("PRODUCTION", default=False, cast=bool)

APPS = [
    'widget_tweaks',
    'smart_selects',
    'debug_toolbar',
    'accounts',
    'webapp',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher'
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'webapp:index'
LOGOUT_REDIRECT_URL = 'webapp:index'
LOGIN_URL = 'accounts:login'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACTIVATE_USERS_EMAIL = False


MEDIA_ROOT = os.path.join(BASE_DIR, '../../uploads')
MEDIA_URL = '/media/'

USE_DJANGO_JQUERY = True


if not PRODUCTION:
    from .local import *
else:
    from .prod import *

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
