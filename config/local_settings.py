# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'user_management',
        'USER': 'user_management',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}