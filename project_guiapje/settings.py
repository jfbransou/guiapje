"""
Django settings for project_guiapje project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import logging
from dotenv import load_dotenv
from datetime import datetime

hora_atual = datetime.now().strftime("%H:%M:%S")
logging.warning('>>>>> Teste de log: o sistema de logs está funcionando corretamente!' + hora_atual)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR.parent / 'guia-pje/.env'

load_dotenv(dotenv_path=dotenv_path)

#logging.warning('>>>>> DOTENV_PATH ====== ' + str(dotenv_path))

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'jfbransou.pythonanywhere.com'
]
#'localhost',
#'www.guiapje.com.br',
#'67.207.91.222',
#'guiapje.com.br',


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project_guiapje.app_core',
    'project_guiapje.app_guiapje',
    'project_guiapje.app_accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_guiapje.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'project_guiapje/app_core/templates')],
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

WSGI_APPLICATION = 'project_guiapje.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('DATABASE_NAME')),
        'USER': str(os.getenv('DATABASE_USER')),
        'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
        'HOST': str(os.getenv('DATABASE_HOST')),
        'PORT': str(os.getenv('DATABASE_PORT')),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


#STATIC_ROOT = os.path.join(BASE_DIR, 'project_guiapje/static')
STATIC_ROOT = os.path.join(BASE_DIR, 'project_guiapje/staticfiles')

#STATIC_ROOT = "/home/myusername/myproject/static"
# or, eg,
#STATIC_ROOT = os.path.join(BASE_DIR, "static")

# O STATICFILES_DIRS informa ao Django onde procurar arquivos estáticos além das pastas static/ nas aplicações.
STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'project_guiapje/static'), # Pasta global 'static' no diretório do PROJETO
    os.path.join(BASE_DIR, 'project_guiapje/app_core/static'), # Pasta 'static' da APLICAÇÃO app_core
    os.path.join(BASE_DIR, 'project_guiapje/app_guiapje/static'), # Pasta 'static' da APLICAÇÃO app_guiapje
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# URL para acessar os arquivos estáticos no navegador
STATIC_URL = '/static/'

print(f"BASE_DIR ======= : ", BASE_DIR)
print(f"STATIC_ROOT ======= : ", STATIC_ROOT)
print(f"STATICFILES_DIRS: =============: ", STATICFILES_DIRS)
print(f"STATIC_URL ======= : ", STATIC_URL)

# Comando python3 manage.py findstatic --verbosity 2

# Comando: python3 manage.py collectstatic:
# Esse comando copia todos os arquivos estáticos (de todas as pastas static/ nas APLICAÇÕES e no diretório global do PROJETO) para o diretório especificado na variável STATIC_ROOT

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'project_guiapje','media')

# Configurações para o Email

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # simular envio via console
#Email
EMAIL_BACKEND = str(os.getenv('EMAIL_BACKEND'))
DEFAULT_FROM_EMAIL = str(os.getenv('DEFAULT_FROM_EMAIL'))
EMAIL_USE_TLS = str(os.getenv('EMAIL_USE_TLS'))
EMAIL_HOST = str(os.getenv('EMAIL_HOST'))
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = str(os.getenv('EMAIL_PORT'))
#CONTACT_EMAIL = str(os.getenv('CONTACT_EMAIL')) # destinatário do email...

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'app_accounts:login'
LOGIN_REDIRECT_URL = 'app_core:home'
LOGOUT_URL = 'app_accounts:logout'
LOGOUT_REDIRECT_URL = 'app_core:home'

AUTH_USER_MODEL = "app_accounts.User"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/home/jfbransou/guia-pje/error.log',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/jfbransou/guia-pje/error.log',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/jfbransou/guia-pje/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file_warning','file_debug','file_error'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
