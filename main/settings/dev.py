from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []

THIRD_PARTY_APPS = [
    "debug_toolbar",
]

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [ 
    "127.0.0.1", 
]
