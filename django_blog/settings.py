"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8q@q!u=s#vgqz7=s)2au6w4ae@4mt8i=#76x6ll-x_jbs-_zh%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.aaron-zhao.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.weibo',
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

ROOT_URLCONF = 'django_blog.urls'

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
                'blog.views.global_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        "PASSWORD": 'mangui710',
        'HOST': '127.0.0.1',
        'PORT': '3700',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog/static'),
]

# Media root 设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 富文本编辑器设置
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'language':'zh-cn',
        'width': '750px',
        'height': '500px',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
                       '-','JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor', '-', 'RemoveFormat']},
            {'name': 'insert',
             'items': ['Image', '-', 'Flash', 'Iframe', '-', 'Table', 'CodeSnippet', 'Templates']},
            '/',
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'special', 'items': ['Subscript', 'Superscript', '-', 'HorizontalRule',
                                          'SpecialChar', 'Smiley']},
            {'name': 'tools', 'items': ['Undo', 'Redo', '-', 'Source', 'Preview', 'Save', '-', 'Maximize']}
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet',
                'uploadimage',
                'uploadfile',
                'prism',
            ]),
    }
}

# 自定义日志输出信息
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}  #日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/all.log',     #日志输出文件
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,                         #备份份数
            'formatter':'standard',                   #使用哪种formatters日志格式
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/error.log',
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'log/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'blog.views': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
'''
# Website INFO  Global Var
SITE_NAME = 'Python学习、Django技术交流与分享-AA的博客'
SITE_DESCP = 'AA的博客是分享学习Python技术与经验的个人博客，由Python、Django以及资源分享等分类组成，内容主要是Django博客开发。'
SITE_KEYWORDS = 'AA的博客, Python技术分享, Django博客开发, Django技术交流'

# 自定义用户model
AUTH_USER_MODEL = 'blog.user'

# django-allauth相关设置
AUTHENTICATION_BACKENDS = (
# django admin所使用的用户登录与django-allauth无关
    'django.contrib.auth.backends.ModelBackend',

# `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 前面我们app里添加了django.contrib.sites,需要设置SITE_ID
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

# Email setting
# SMTP服务器，我使用的是sendclound的服务
EMAIL_HOST = 'smtp.sendcloud.net'
EMAIL_HOST_USER = 'Aaroon_test_N05MI9'
EMAIL_HOST_PASSWORD = 'u7qFYbkRKK08PMtR'
EMAIL_PORT = 25
# 是否使用了SSL 或者TLS
#EMAIL_USE_SSL = True
#EMAIL_USE_TLS = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost
DEFAULT_FROM_EMAIL = 'Aaron-Zhao <noreply@aaron-zhao.com>'