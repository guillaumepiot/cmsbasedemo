import os

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Guillaume Piot', 'support@cotidia.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev/cmsbasedemo.db',                      # Or path to database file if using sqlite3.
    }
}

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, '../../media/')
MEDIA_URL = '/media/'

# Static root will be used for collecting static files for production deployment
# Use the command: python manage.py collectstatic
STATIC_ROOT = os.path.join(PROJECT_DIR, '../../static/')

STATIC_URL = '/static/'

# Here's where we save the project static files
# Not be served in production mode
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "../static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1k_m3knstxukh^f_tm1lsn347q(yo__oq=q_w#ornf3omg*pfk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    # Language switcher management
    'localeurl.middleware.LocaleURLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "cmsbasedemo.context_processor.website_settings"
)

ROOT_URLCONF = 'cmsbasedemo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cmsbasedemo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, '../templates/'),
)

INSTALLED_APPS = (

    'admin_tools',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'admin_tools.liststyle',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'cmsbase',
    'reversion',
    'mptt',
    'south',
    'redactor',
    'filemanager'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHOR_URL = 'http://example.com'
AUTHOR = 'Author'

ADMIN_TOOLS_INDEX_DASHBOARD = 'cmsbasedemo.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_MENU = 'cmsbasedemo.menu.CustomMenu'

LANGUAGES = (
    ('en', 'English'),
    # ('nl', 'Dutch'),
    # ('es', 'Spanish'),
    # ('pt', 'Portuguese'),
    # ('de', 'German'),
)
DEFAULT_LANGUAGE = LANGUAGES[0][0]

# Set the django language code to the default language
LANGUAGE_CODE = DEFAULT_LANGUAGE

# Define wether or not to display the url prefix
# False if we have only one language supported
PREFIX_DEFAULT_LOCALE = False if len(LANGUAGES) <= 1 else True
