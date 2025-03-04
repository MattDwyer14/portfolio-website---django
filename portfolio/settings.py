from pathlib import Path
import os
from dotenv import load_dotenv
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

AZURE_DEPLOYMENT = os.getenv('AZURE_DEPLOYMENT') == 'true'

# Only load .env.secrets in local development
if not AZURE_DEPLOYMENT:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env.secrets')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY')

if AZURE_DEPLOYMENT:
    DEBUG = False
    # Load ALLOWED_HOSTS from environment variable and ensure it's a list
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
    # Ensure that CSRF_TRUSTED_ORIGINS is correctly populated based on ALLOWED_HOSTS
    CSRF_TRUSTED_ORIGINS = [f'https://{host.strip()}' for host in ALLOWED_HOSTS if host.strip()]
    
else:
    DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    CSRF_TRUSTED_ORIGINS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'projects'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add template dirs here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

if AZURE_DEPLOYMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.getenv('DB_HOST'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
if AZURE_DEPLOYMENT:
    # Production: Azure Storage

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "account_name": os.getenv('AZURE_ACCOUNT_NAME'),
                "account_key": os.getenv('AZURE_ACCOUNT_KEY'),
                "azure_container": "portfoliomedia"  # Media files here
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.azure_storage.AzureStorage",
            "OPTIONS": {
                "account_name": os.getenv('AZURE_ACCOUNT_NAME'),
                "account_key": os.getenv('AZURE_ACCOUNT_KEY'),
                "azure_container": "portfoliostatic"  # Static files here
            },
        },
    }

    # Set URLs based on the storage settings
    # If using Managed Identity and a public container, you can directly access them via a custom domain if set
    STATIC_URL = f"https://{os.getenv('AZURE_ACCOUNT_NAME')}.blob.core.windows.net/{os.getenv('AZURE_CONTAINER', 'static')}/"
    MEDIA_URL = f"https://{os.getenv('AZURE_ACCOUNT_NAME')}.blob.core.windows.net/{os.getenv('AZURE_MEDIA_CONTAINER', 'media')}/"



else:
    # Development (local static files)
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [
        BASE_DIR / 'core/static/core',
        BASE_DIR / 'projects/static/projects',
    ]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
