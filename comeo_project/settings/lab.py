from .common import *
from neomodel import config
config.DATABASE_URL = 'bolt://neo4j:neo4j@neo:7687'
config.ENCRYPTED_CONNECTION = False


DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_collected')

# Custom email backend which supports ssl connection supported by zoho
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@comeo.co'
EMAIL_HOST_PASSWORD = ENV_EMAIL_HOST_PASSWORD

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"

INSTALLED_APPS += ('apps.comeo_debug',)
