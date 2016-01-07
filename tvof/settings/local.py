DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app_tvof_dev',
        'USER': 'app_tvof',
        'PASSWORD': 'Wh1teR4bbit',
        'ADMINUSER': 'postgres',
        'HOST': 'db-pggis-1.cch.kcl.ac.uk'
    },
}

INTERNAL_IPS = ('0.0.0.0', '127.0.0.1', '::1')

SECRET_KEY = '12345'

FABRIC_USER = 'njakeman'

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
