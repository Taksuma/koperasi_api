import os
import dj_database_url
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Ambil SECRET_KEY dari environment variable. Railway akan menyediakannya.
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Atur DEBUG berdasarkan environment variable. Default-nya False.
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Atur ALLOWED_HOSTS dari environment variable jika perlu,
# atau gunakan ['*'] untuk Railway jika Anda tidak tahu domain pastinya.
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # Tambahkan ini untuk static files
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'members',
    'deposits',
    'loans',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Harus setelah SecurityMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... (sisa MIDDLEWARE)

ROOT_URLCONF = 'koperasi_api.urls'

# ... (sisa TEMPLATES)

WSGI_APPLICATION = 'koperasi_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
if 'RAILWAY_ENVIRONMENT' in os.environ or 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=False)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ... (sisa AUTH_PASSWORD_VALIDATORS, I18N, etc.)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True

# CSRF configuration
# Ganti dengan domain production Anda
CSRF_TRUSTED_ORIGINS = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1:8000').split(',')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY, # Gunakan SECRET_KEY dari atas
    # ... (sisa konfigurasi SIMPLE_JWT)
}