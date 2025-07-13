import os
from django.utils.translation import gettext_lazy as _
from decouple import config, Csv
from unipath import Path
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ADMINS = config('ADMINS', default='', cast=lambda val: [('Admin', tk.strip()) for tk in val.split(',')])

TEMPLATE_DEBUG = config('TEMPLATE_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

IS_API = config('IS_API', default=False, cast=bool)

API_URL = config('API_URL', default='')

# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    

# app pour django-allauth
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # ce provider sert a authentification via Google
    'allauth.socialaccount.providers.telegram', # ce provider sert a authentification via Telegram
    'allauth.socialaccount.providers.facebook', # ce provider sert a authentification via Facebook

# app personnel
    'log' 
]

AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:////' + BASE_DIR.child('') + '?conn_max_age=0',
        cast=lambda val: db_url(val.split('?')[0], conn_max_age=int(val.split('?')[1].replace('conn_max_age=', '')))
    ),
    'umbrella': config(
        'UMBRELLA_DATABASE_URL',
        default='sqlite:////' + BASE_DIR.child('') + '?conn_max_age=0',
        cast=lambda val: db_url(val.split('?')[0], conn_max_age=int(val.split('?')[1].replace('conn_max_age=', '')))
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND', default='django.core.cache.backends.memcached.PyMemcacheCache'),
        'LOCATION': config('CACHE_LOCATION', default='127.0.0.1:11211'),
        'TIMEOUT': config('CACHE_TIMEOUT', default=300, cast=int),
        'KEY_PREFIX': config('CACHE_KEY_PREFIX', default='prefix'),  # Use rather svdprod for Production
        'VERSION': config('CACHE_VERSION', default='1')
    }
}



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='Africa/Douala')

USE_I18N = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

ACCOUNT_FORMS = {
    'login': 'log.forms.BootstrapLoginForm',
    'signup': 'log.forms.BootstrapSignupForm',
}

USE_L10N = True

USE_TZ = config('USE_TZ', default=True, cast=bool)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR + '/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'media/'

STATIC_URL = 'static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

LOCAL_DEV = config('LOCAL_DEV', default=False, cast=bool)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'home'

ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']

SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Configuration allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'


LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
