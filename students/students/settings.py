#import os
import os.path

from pathlib import Path

import django.core.mail.backends.console
#from dotenv import load_dotenv


#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#load_dotenv()

#SECRET_KEY = os.getenv('SECRET_KEY')
print(f'{SECRET_KEY=}')

#DEBUG = True
DEBUG = False

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['matfak82.uz','www.matfak82.uz','95.130.227.79']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apprasm.apps.ApprasmConfig',    # Приложение альбом
    'appvideo.apps.AppvideoConfig',  # Приложение видео
    'appusers.apps.AppusersConfig',  # Авторизация и аутентификация
    'appkurs.apps.AppkursConfig',    # Однакурсники
]
INSTALLED_APPS += [
    'django_extensions',            # Это для работы оболочки  (python manage.py shell_plus --print-sql)
#    'debug_toolbar',                # AAA После   pip install django-debug-toolbar
]

MIDDLEWARE = [
#    'debug_toolbar.middleware.DebugToolbarMiddleware',          # AAA
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',     # для Регистрации и авторизации
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # для Регистрации и авторизации
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#INTERNAL_IPS = ["127.0.0.1",]  # AAA

ROOT_URLCONF = 'students.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 'Это для того чтобы base_site.html в админ панеле отсюда бралось
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'appusers.context_processors.get_rasm_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'students.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'kursdb',
    'USER': 'kursdosh',
    'PASSWORD': 'rasul_matfak82_kursdosh',
    'HOST': 'localhost',
    'PORT': '5432',
    }
}
'''




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

LANGUAGE_CODE = 'ru' # = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#--------------------------------------------------------------------------------------------------

STATIC_URL = 'static/'  # для статических файлов добавляем и в корне проекта создадим папку static

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static',]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# [***]  в urls.py делаем добавление
MEDIA_URL ='media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
#--------------------------------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'users:login'

# BBB. Напишем свой backend для авторизации по email (appusers->authentication.py)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend' , # авторизация по умолчание (здесь указали явно)
    'appusers.authentication.EmailAuthBackend',   # авторизация пользователский Backend
]

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL= EMAIL_HOST_USER
EMAIL_ADMIN= EMAIL_HOST_USER


#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'me@gmail.com'
#EMAIL_HOST_PASSWORD = 'password'