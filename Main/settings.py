import os

from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = [
    'rivesuvacrispa.pythonanywhere.com',
    '127.0.0.1',
    'chrome-extension://kgafifkmgpbjhnflbjlhaochngjamlgm'
]

INSTALLED_APPS = [
    'CollectionApp',
    'Main',

    'corsheaders'
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'Main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH_CLIENT_SECRET')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'chrome-extension://kgafifkmgpbjhnflbjlhaochngjamlgm',
    'rivesuvacrispa.pythonanywhere.com'
)
