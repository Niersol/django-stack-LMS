from .common import *

SECRET_KEY = 'django-insecure-ulj4#fa)p%h)utvw&#=52v8q#m_%r#f#nk!ad$c@phdz)i(z6i'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "library_management",
        "USER": "postgres",
        "PASSWORD": "45645688mm",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
