from .settings import *

DEBUG = False

# Crie a secret key para seu ambiente de produção
SECRET_KEY = 'ixb97()lun&#ts=&b4t2u%p1_62-!8dw2j==j)d^3-j$!z(@*m+-h'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
