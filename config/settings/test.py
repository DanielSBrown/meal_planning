"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import BASE_DIR, env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="E0g2X89nuF6E8Av23PLA7bsFaSQtpM2MSZlwUryaHkWuga3sLyXip12F0zKYSmie",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"
# So the app domain is available on a per environment basis
SITE_DOMAIN = "https://meal_planning.test"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# Enables template coverage to happen in the test environment
TEMPLATES[-1]["OPTIONS"]["debug"] = True  # type: ignore[index] # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------
TEST = True

MEDIA_ROOT = str(BASE_DIR / "media/test")
