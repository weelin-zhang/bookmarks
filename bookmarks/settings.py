"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!o5%x&4ggf%3-!1rvr#s7)s@6g=a3%e!m4cfw@if2!+3co!k7('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
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

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


'''
MEDIA_URL 是管理用户上传的多媒体文件的主URL，MEDIA_ROOT是这些文件在本地保存的路径
我们动态的构建这些路径相对我们的项目路径来确保我们的代码更通用化。
'''
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AUTH_USER_MODEL = "auth.User"

# 自定义认证后端
'''
我们保留默认的ModelBacked用来保证用户仍然可以通过用户名和密码进行认证，
接着我们包含进了我们自己的email-based认证（authentication）后台
'''
AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
   'account.authentication.EmailAuthBackend',
   'account.authentication.LDAPAuthBackend',
)


STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
)


# ldap
# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap://192.168.20.104:389"

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "ou=People,dc=srv,dc=world"


# 缓存设置
'''
BACKEND：使用的缓存后端。
KEY_FUNCTION：包含一个指向回调函数的点路径的字符，这个函数以prefix(前缀)、verision(版本)、和 key (键) 作为参数并返回最终缓存键（cache key）。
KEY_PREFIX：一个用于所有缓存键的字符串，避免冲突。
LOCATION：缓存的位置。基于你的缓存后端，这可能是一个路径、一个主机和端口，或者是内存中后端的名字。
OPTIONS：任何额外的传递向缓存后端的参数。
TIMEOUT：默认的超时时间，以秒为单位，用于储存缓存键。默认设置是 300 秒，也就是五分钟。如果把它设置为 None ，缓存键将不会过期。
VERSION：默认的缓存键的版本。对于缓存版本是很有用的
'''

'''
Memcached中的key-value:

stats cachedump 1 10
ITEM prefix_:1:niubi [3 b; 1531123840 s]
ITEM :1:niubi [3 b; 1531123729 s]
ITEM userId [5 b; 0 s]
'''
# CACHES = {
    # 'default': {
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': './aaa'

        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '192.168.20.104:11211',
        # 'KEY_PREFIX': "prefix_"
    # }
# }


'''
# redis 127.0.0.1:6379[15]> keys *
1) ":1:rediskey01"
'''
CACHES = {
    "default": {
        # "BACKEND": "django_redis.cache.RedisCache",
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.20.104:6379/15",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
            "PASSWORD": 'xxxxxx'
        }
    }
}
