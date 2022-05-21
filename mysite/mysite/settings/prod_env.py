from .base_env import *


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'dlckdtjr55',
        'HOST': 'localhost',
        'PORT': '', # 5432 default
    }
}
