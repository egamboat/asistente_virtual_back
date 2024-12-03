"""
Django settings for asistente_virtual_backend project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env.local'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY ='django-insecure-tdp&vw#7dok1$_v3=b%@e7q_w@y(7z2^m=9+1segay$!akah4l'
SECRET_KEY= os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DEBUG', False).lower() == 'true'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'asistente',
    'usuario',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'asistente_virtual_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'asistente_virtual_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


import dj_database_url
database_url = os.environ.get('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.parse(database_url)
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'asistente_virtual',
#         'USER': 'postgres',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),  # Duración del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Duración del token de refresco
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    # Configura el algoritmo y la clave secreta
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

CORS_ALLOW_ALL_ORIGINS = True

JAZZMIN_SETTINGS = {
    "site_title": "Asistente Nomi Admin",
    "site_header": "Asistente Nomi",
    "site_brand": "Asistente Nomi",
    "site_logo": "img/mic_white.png",  # Ruta estática
    "login_logo": "img/logo_negro.png",  # Imagen en el login
    "login_logo_dark": "img/logo_negro.png",  # Imagen en modo oscuro
    "site_logo_classes": "img-circle",
    "welcome_sign": "Bienvenido al Admin de Nomi",
    "copyright": "Asistente Nomi",
    "custom_css": "css/custom_admin.css",
    "icons": {
        # Íconos para los modelos de tu app "asistente"
        "asistente.agenda": "fas fa-calendar-alt",   # Ícono de calendario
        "asistente.evento": "fas fa-calendar-check", # Ícono de evento
        "asistente.modalidad": "fas fa-cogs",        # Ícono de configuración
        "asistente.tipoevento": "fas fa-tags",       # Ícono de etiquetas
        # Íconos para modelos de autenticación
        "auth.user": "fas fa-user",                  # Ícono de usuario
        "auth.group": "fas fa-users",                # Ícono de grupo
    },
}
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]