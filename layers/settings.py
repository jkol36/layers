"""
Django settings for layers project.

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
SECRET_KEY = 'xtr$+&)$@h28=qc%=z%wqhlf5%t=jinxl0zil%8qp3dvy3+#$n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

LOCAL = False

TEMPLATE_DEBUG = False




INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'layers.profiles',
    'layers.projects',
    'layers.landing',
    'layers.get_started',
    'layers.contact',
    'layers.subscribe',
    'sorl.thumbnail',

)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'layers.urls'

WSGI_APPLICATION = 'layers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if DEBUG == True and LOCAL == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }

else:
    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME':'layers_db',
            'USER': 'layers_django',
            'PASSWORD':'StoreTheLayers',
            'HOST':'localhost',
            'PORT':'',
            },
        }

if LOCAL == False:
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
#allowed hosts
ALLOWED_HOSTS = ['*']
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

### 404 error page



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'layers/templates'),
    )
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'layers/static/'),
)


STATIC_URL = '/static/'
STATIC_ROOT = '/webapps/layers_django/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/webapps/layers_django/media/'
AUTH_USER_MODEL = 'profiles.Profile'

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
    'django.template.loaders.filesystem.Loader', 
    'django.template.loaders.app_directories.Loader',)),
    'django.template.loaders.eggs.Loader',
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/webapps/layers_django/logs/debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}



