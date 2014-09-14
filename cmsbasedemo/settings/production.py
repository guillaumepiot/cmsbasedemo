from cmsbasedemo.settings import * 

DEBUG=False
TEMPLATE_DEBUG=DEBUG

ALLOWED_HOSTS = ['demo.cmsbase.cotidia.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, '../../dev/cmsbasedemo_live.db'),                      # Or path to database file if using sqlite3.
    }
}