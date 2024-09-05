"""
Django settings for fisa_django project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.utils import timezone
import os
from dotenv import load_dotenv 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET')
# AWS S3 설정
AWS_ACCESS_KEY_ID = os.getenv('S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_S3_REGION_NAME =  os.getenv('S3_REGION')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "board", # 마지막 줄에도 기왕이면 ,를 적어주세요
    # "account",
    'allauth',
    'allauth.account',
    'crispy_forms',
    "crispy_bootstrap5",
    "debug_toolbar",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
     "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "fisa_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fisa_django.wsgi.application"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": os.getenv('DB_ENGINE'),
        "NAME": os.getenv('DB_NAME'), # DB Name
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST'),
        "PORT": os.getenv('DB_PORT'),
    },
     'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'" #  MySQL 데이터베이스의 초기 설정 명령어
         },                                                       # STRICT_TRANS_TABLES: 트랜잭션을 지원하는 테이블, 
                                                                  # 잘못된 데이터가 삽입되거나 업데이트될 때 경고 대신 오류를 발생
 }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/



# 향후 django app 내에서 현재시각을 사용할 때는 
# datetime 대신 아래 방식으로 시간을 사용해주세요
now = timezone.now()
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = 'Asia/Seoul'

# i18n은 "internationalization"의 약자로, 장고에서 다국어 지원 및 지역화 기능을 제공합니다. 이를 통해 웹 애플리케이션이 여러 언어와 문화권에서 사용될 수 있도록 합니다. 주요 기능은 다음과 같습니다:
# 번역: 텍스트를 여러 언어로 번역할 수 있습니다.
# 지역화: 날짜, 시간, 숫자, 통화 등의 형식을 사용자의 지역에 맞게 변환합니다.
# 언어 선택: 사용자가 선호하는 언어를 선택할 수 있게 합니다.
USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# STATIC_URL = "static/"
# MEDIA_URL = '/media/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
# MEDIA_ROOT = os.path.join(BASE_DIR, '_media') 
STATICFILES_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"

MEDIAFILES_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"


STORAGES = {
    "default": {"BACKEND": "fisa_django.custom_storage.MediaStorage"},
    "staticfiles": {"BACKEND": "fisa_django.custom_storage.StaticStorage"},
}

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=2592000", # 30일(30 * 24 * 60 * 60)을 의미,  S3에 업로드된 객체가 브라우저나 캐시 서버에 의해 30일 동안 캐시될 수 있도록 합니다. 이를 통해 웹사이트의 성능을 향상시킵니다.
}



# 'blog/post-list'
# LOGIN_REDIRECT_URL =  # locahost:8000/login/account/blog/post-list
LOGIN_REDIRECT_URL = 'blog_app:post_list'  # 로그인성공시 보내줄 리다이렉트 주소

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

INTERNAL_IPS = [
    "127.0.0.1",
]


# 디버깅을 위한 출력
# print(f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")  # 디버깅
# print(f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")  # 디버깅
# print(f"AWS_STORAGE_BUCKET_NAME: {AWS_STORAGE_BUCKET_NAME}")  # 디버깅
# print(f"STATICFILES_STORAGE: {STATICFILES_LOCATION}")  # 디버깅


