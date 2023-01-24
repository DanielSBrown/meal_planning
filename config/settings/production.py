from .base import *  # noqa
from .base import BASE_DIR, env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

# CACHES
# ------------------------------------------------------------------------------
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": env("REDIS_URL"),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             # Mimicing memcache behavior.
#             # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
#             "IGNORE_EXCEPTIONS": True,
#         },
#     }
# }

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# # STORAGES
# # ------------------------------------------------------------------------------
# # https://django-storages.readthedocs.io/en/latest/#installation
INSTALLED_APPS += ["storages"]  # noqa F405

AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)

AWS_QUERYSTRING_AUTH = False

# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
}

# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

DEFAULT_FILE_STORAGE = "apps.core.storages.MediaRootS3Boto3Storage"
MEDIA_URL = f"https://{aws_s3_domain}/media/"


# STATIC
# ------------------------
# STATICFILES_STORAGE = "apps.utils.storages.StaticRootS3Boto3Storage"
COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
# STATIC_URL = f"https://{aws_s3_domain}/static/"
# MEDIA
# ------------------------------------------------------------------------------

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Meal Planning Team <noreply@example.com>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Meal Planning]",
)

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = "admin/"

# # Anymail
# # ------------------------------------------------------------------------------
# # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
# INSTALLED_APPS += ["anymail"]  # noqa F405
# # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# # https://anymail.readthedocs.io/en/stable/esps/mailgun/
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# ANYMAIL = {
#     "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
#     "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
#     "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
# }

# Collectfast
# ------------------------------------------------------------------------------
# https://github.com/antonagestam/collectfast#installation
INSTALLED_APPS = ["collectfast"] + INSTALLED_APPS  # noqa F405

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "log/django.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
