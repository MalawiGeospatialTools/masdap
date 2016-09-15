# -*- coding: utf-8 -*-
import os
from geonode.settings import *

SITENAME = 'masdap'

LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "masdap.wsgi.application"

GEONODE_APPS = (
    # GeoNode internal apps
    'geonode.people',
    'geonode.base',
    'geonode.layers',
    'geonode.maps',
    'geonode.proxy',
    'geonode.security',
    'geonode.social',
    'geonode.catalogue',
    'geonode.documents',
    'geonode.api',
    'geonode.groups',
    'geonode.services',

    # GeoServer Apps
    # Geoserver needs to come last because
    # it's signals may rely on other apps' signals.
    'geonode.geoserver',
    'geonode.upload',
    'geonode.tasks'
)

INSTALLED_APPS = (

    # Boostrap admin theme
    # 'django_admin_bootstrapped.bootstrap3',
    # 'django_admin_bootstrapped',

    # Apps bundled with Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.gis',

    # Third party apps

    # Utility
    'pagination',
    'taggit',
    'friendlytagloader',
    'geoexplorer',
    'leaflet',
    'django_extensions',
    # 'haystack',
    'autocomplete_light',
    'mptt',
    'modeltranslation',
    'djcelery',

    # Theme
    "pinax_theme_bootstrap_account",
    "pinax_theme_bootstrap",
    'django_forms_bootstrap',

    # Social
    'account',
    'avatar',
    'dialogos',
    'agon_ratings',
    #'notification',
    'announcements',
    'actstream',
    'user_messages',
    'tastypie',
    'polymorphic',
    'guardian',
    
    #Contact
    'contact',
    'nocaptcha_recaptcha',

) + GEONODE_APPS

#EMAIL SERVICE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your.smtp.server'  
DEFAULT_FROM_EMAIL = 'your.account@email.com'
EMAIL_HOST_USER = 'your.account@smtp.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587 #check port
EMAIL_USE_TLS = True #check tls


#RECAPTCHA SERVICE

NORECAPTCHA_SITE_KEY = "norecaptcha_site_key"
NORECAPTCHA_SECRET_KEY = "norecaptcha_secret_key"
NORECAPTCHA_VERIFY_URL = "norecaptcha_verify_url"




try:
    from local_settings import *
except ImportError:
    pass

STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

ROOT_URLCONF = 'masdap.urls'

LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

