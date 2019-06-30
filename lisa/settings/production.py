import os
from decouple import config
from lisa.settings.common import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('MYSQL_DATABASE'),
#         'USER': config('MYSQL_USER'),
#         'PASSWORD': config('MYSQL_PASSWORD'),
#         'HOST': 'db',
#         'PORT': 3306,
#     }
# }


#configs para o heroku
cwd = os.getcwd()
if cwd == '/app' or cwd[:4] == '/tmp':
    import dj_database_url
    DATABASES = {
    'default':dj_database_url.config(default='postgres://localhost')
    }
    # Honra o cabecalho 'X-forwarded-proto' para request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    #cabecalhos para permitir todos os hosts
    ALLOWED_HOSTS = ['*']
    DEBUG = True
    #configs de recursos estaticos
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'