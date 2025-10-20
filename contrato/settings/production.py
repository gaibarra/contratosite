from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Hosts/domains allowed to serve
ALLOWED_HOSTS = [
    'contratosmodelo.site',
    'www.contratosmodelo.site',
    '0.0.0.0',
    '127.0.0.1',
    '194.113.64.91',
    'contratosmodelo.link',
]

# CSRF and proxy settings for HTTPS behind Nginx
CSRF_TRUSTED_ORIGINS = [
    'https://contratosmodelo.site',
    'https://www.contratosmodelo.site',
    'https://contratosmodelo.link',
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
# Make these configurable so runserver can work without HTTPS
SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', '1') == '1'
SESSION_COOKIE_SECURE = os.getenv('DJANGO_SESSION_COOKIE_SECURE', '1') == '1'
CSRF_COOKIE_SECURE = os.getenv('DJANGO_CSRF_COOKIE_SECURE', '1') == '1'

# Security hardening (HTTPS-only sites)
SECURE_HSTS_SECONDS = 63072000  # 2 years
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
X_FRAME_OPTIONS = 'DENY'

# Remove debug toolbar in production
try:
    INSTALLED_APPS.remove('debug_toolbar')
except ValueError:
    pass
MIDDLEWARE = [m for m in MIDDLEWARE if m != 'debug_toolbar.middleware.DebugToolbarMiddleware']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'd7p6erb1fvqq0v',
#        'HOST': 'ec2-44-207-133-100.compute-1.amazonaws.com',
#        'USER': 'igeypucwdvfkvl',
#        'PASSWORD': '0ce2682f24f296e645956e80e0c564cee0f52662c9be84c987d9b8f457ad5d7b',
#        'PORT': 5432
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contrato',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '6Vlgpcr&',
        'PORT': 5432
    }
}


#import dj_database_url
#from decouple import config

#DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )

#}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
