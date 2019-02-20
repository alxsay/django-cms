import os

# BASE_DIR is pointing to the parent directory of PROJECT_ROOT. You can re-write the two definitions as:
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(PROJECT_ROOT)
BASE_DIR = os.path.dirname(
            os.path.dirname(
            os.path.dirname(
            os.path.abspath(__file__))))


SECRET_KEY = '1^x$gh7&497&*7gv1pkpau%ovcio=)jrv!=t!nq#2tv!3esp-c'

#DEBUG = True

#ALLOWED_HOSTS = [ '127.0.0.1' ]

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_dashboard',
    'app',
    'chat',
    'cms'
]

MIDDLEWARE = [
    'app.middleware.AppMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_cms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [ os.path.join( BASE_DIR, 'jinja2' ) ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'django_cms_project.jinja2.environment'
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join( BASE_DIR, 'templates' ) ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

WSGI_APPLICATION = 'django_cms_project.wsgi.application'
ASGI_APPLICATION = "django_cms_project.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('localhost', 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# https://docs.djangoproject.com/en/2.1/topics/db/multi-db/
#DATABASE_ROUTERS = [ 'app.database.router.AuthRouter', 'app.database.router.PrimaryReplicaRouter' ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    )
}


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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join( BASE_DIR, 'static_media' ) ]
VENV_PATH = os.path.dirname( BASE_DIR )
STATIC_ROOT = os.path.join( VENV_PATH, 'static_root' )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join( VENV_PATH, 'media' )
