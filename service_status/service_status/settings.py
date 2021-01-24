import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '123')

DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = [os.environ.get('INTERNAL_SERVICES_ALLOWED_HOSTS', 'localhost')]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'handlers'
]

ROOT_URLCONF = 'handlers.urls'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

WSGI_APPLICATION = 'service_status.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'service_status',
        'USER' : 'postgres',
        'PASSWORD' : '123456789',
        'HOST' : '178.154.253.159',
        'PORT' : 5432,
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
