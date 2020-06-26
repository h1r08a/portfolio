from .settings_common import *

DEBUG = True
ALLOWED_HOSTS = []
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Email送信先（開発環境だからコンソールへ）
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')