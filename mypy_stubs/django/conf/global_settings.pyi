# Stubs for django.conf.global_settings (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def gettext_noop(s: Any): ...

DEBUG: bool
DEBUG_PROPAGATE_EXCEPTIONS: bool
ADMINS: Any
INTERNAL_IPS: Any
ALLOWED_HOSTS: Any
TIME_ZONE: str
USE_TZ: bool
LANGUAGE_CODE: str
LANGUAGES: Any
LANGUAGES_BIDI: Any
USE_I18N: bool
LOCALE_PATHS: Any
LANGUAGE_COOKIE_NAME: str
LANGUAGE_COOKIE_AGE: Any
LANGUAGE_COOKIE_DOMAIN: Any
LANGUAGE_COOKIE_PATH: str
USE_L10N: bool
MANAGERS = ADMINS
DEFAULT_CONTENT_TYPE: str
DEFAULT_CHARSET: str
FILE_CHARSET: str
SERVER_EMAIL: str
DATABASES: Any
DATABASE_ROUTERS: Any
EMAIL_BACKEND: str
EMAIL_HOST: str
EMAIL_PORT: int
EMAIL_USE_LOCALTIME: bool
EMAIL_HOST_USER: str
EMAIL_HOST_PASSWORD: str
EMAIL_USE_TLS: bool
EMAIL_USE_SSL: bool
EMAIL_SSL_CERTFILE: Any
EMAIL_SSL_KEYFILE: Any
EMAIL_TIMEOUT: Any
INSTALLED_APPS: Any
TEMPLATES: Any
FORM_RENDERER: str
DEFAULT_FROM_EMAIL: str
EMAIL_SUBJECT_PREFIX: str
APPEND_SLASH: bool
PREPEND_WWW: bool
FORCE_SCRIPT_NAME: Any
DISALLOWED_USER_AGENTS: Any
ABSOLUTE_URL_OVERRIDES: Any
IGNORABLE_404_URLS: Any
SECRET_KEY: str
DEFAULT_FILE_STORAGE: str
MEDIA_ROOT: str
MEDIA_URL: str
STATIC_ROOT: Any
STATIC_URL: Any
FILE_UPLOAD_HANDLERS: Any
FILE_UPLOAD_MAX_MEMORY_SIZE: int
DATA_UPLOAD_MAX_MEMORY_SIZE: int
DATA_UPLOAD_MAX_NUMBER_FIELDS: int
FILE_UPLOAD_TEMP_DIR: Any
FILE_UPLOAD_PERMISSIONS: Any
FILE_UPLOAD_DIRECTORY_PERMISSIONS: Any
FORMAT_MODULE_PATH: Any
DATE_FORMAT: str
DATETIME_FORMAT: str
TIME_FORMAT: str
YEAR_MONTH_FORMAT: str
MONTH_DAY_FORMAT: str
SHORT_DATE_FORMAT: str
SHORT_DATETIME_FORMAT: str
DATE_INPUT_FORMATS: Any
TIME_INPUT_FORMATS: Any
DATETIME_INPUT_FORMATS: Any
FIRST_DAY_OF_WEEK: int
DECIMAL_SEPARATOR: str
USE_THOUSAND_SEPARATOR: bool
NUMBER_GROUPING: int
THOUSAND_SEPARATOR: str
DEFAULT_TABLESPACE: str
DEFAULT_INDEX_TABLESPACE: str
X_FRAME_OPTIONS: str
USE_X_FORWARDED_HOST: bool
USE_X_FORWARDED_PORT: bool
WSGI_APPLICATION: Any
SECURE_PROXY_SSL_HEADER: Any
MIDDLEWARE: Any
SESSION_CACHE_ALIAS: str
SESSION_COOKIE_NAME: str
SESSION_COOKIE_AGE: Any
SESSION_COOKIE_DOMAIN: Any
SESSION_COOKIE_SECURE: bool
SESSION_COOKIE_PATH: str
SESSION_COOKIE_HTTPONLY: bool
SESSION_COOKIE_SAMESITE: str
SESSION_SAVE_EVERY_REQUEST: bool
SESSION_EXPIRE_AT_BROWSER_CLOSE: bool
SESSION_ENGINE: str
SESSION_FILE_PATH: Any
SESSION_SERIALIZER: str
CACHES: Any
CACHE_MIDDLEWARE_KEY_PREFIX: str
CACHE_MIDDLEWARE_SECONDS: int
CACHE_MIDDLEWARE_ALIAS: str
AUTH_USER_MODEL: str
AUTHENTICATION_BACKENDS: Any
LOGIN_URL: str
LOGIN_REDIRECT_URL: str
LOGOUT_REDIRECT_URL: Any
PASSWORD_RESET_TIMEOUT_DAYS: int
PASSWORD_HASHERS: Any
AUTH_PASSWORD_VALIDATORS: Any
SIGNING_BACKEND: str
CSRF_FAILURE_VIEW: str
CSRF_COOKIE_NAME: str
CSRF_COOKIE_AGE: Any
CSRF_COOKIE_DOMAIN: Any
CSRF_COOKIE_PATH: str
CSRF_COOKIE_SECURE: bool
CSRF_COOKIE_HTTPONLY: bool
CSRF_COOKIE_SAMESITE: str
CSRF_HEADER_NAME: str
CSRF_TRUSTED_ORIGINS: Any
CSRF_USE_SESSIONS: bool
MESSAGE_STORAGE: str
LOGGING_CONFIG: str
LOGGING: Any
DEFAULT_EXCEPTION_REPORTER_FILTER: str
TEST_RUNNER: str
TEST_NON_SERIALIZED_APPS: Any
FIXTURE_DIRS: Any
STATICFILES_DIRS: Any
STATICFILES_STORAGE: str
STATICFILES_FINDERS: Any
MIGRATION_MODULES: Any
SILENCED_SYSTEM_CHECKS: Any
SECURE_BROWSER_XSS_FILTER: bool
SECURE_CONTENT_TYPE_NOSNIFF: bool
SECURE_HSTS_INCLUDE_SUBDOMAINS: bool
SECURE_HSTS_PRELOAD: bool
SECURE_HSTS_SECONDS: int
SECURE_REDIRECT_EXEMPT: Any
SECURE_SSL_HOST: Any
SECURE_SSL_REDIRECT: bool
