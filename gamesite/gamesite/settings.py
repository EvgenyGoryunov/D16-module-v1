from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-oge&b4%22%p2$=1_t8a_%18370p&9)c26or3yw&e*6mc6$^g=4'

DEBUG = True

# для регистрации пользователей
ALLOWED_HOSTS = ['127.0.0.1']

# папка для загрузки медиа
CKEDITOR_UPLOAD_PATH = 'uploads/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    # для регистрации пользователя через почту
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # основное приложение
    'main',

    # регистрация пользователей
    'sign',

    # загрузчик медиа
    # https://github.com/django-ckeditor/django-ckeditor  -  пакет находится тут
    # https://www.youtube.com/watch?v=Rh7THG1-THU - смотреть настройку здесь
    'ckeditor',
    'ckeditor_uploader',

]

DEFAULT_FROM_EMAIL = 'factoryskill@yandex.ru'

# добавили для проекта
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # добавили для проекта
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

]

ROOT_URLCONF = 'gamesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# для аутентификации пользователя через почту
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # метод аутентификации через почту
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'gamesite.wsgi.application'

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

USE_TZ = True

# для загрузки фото
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# для загрузки css файлов
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# для регистрации пользователей
# адрес, где находится шаблон аутентификации
# после подтверждения по почте перейдем сюда
# LOGIN_URL = 'sign/login/'
LOGIN_URL = '/accounts/login/'
# перенаправление пользователя после успешного входа на сайт
LOGIN_REDIRECT_URL = '/'

# регистрация и вход по почте
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Модуль 6.3 - подтверждение регистрации через почту
ACCOUNT_AUTHENTIFICTION_METHOD = 'email'


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'factoryskill'
EMAIL_HOST_PASSWORD = 'qazwsx963852'  # пароль от почты
EMAIL_USE_SSL = True