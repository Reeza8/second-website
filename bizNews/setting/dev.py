from bizNews.settings import *

SECRET_KEY = 'django-insecure-(sgf3#@2par*dj_zxq4#jhuba4le&8^#n)xt7=3xe0w6lbp-bp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#sitemap
SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

INSTALLED_APPS+=[
    "debug_toolbar",


]