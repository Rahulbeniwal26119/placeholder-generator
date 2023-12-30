import os
import pathlib

DEBUG = os.environ.get("DEBUG", "on") == "on"

BASE_DIR = pathlib.Path(__file__).parent.parent.resolve()

# SECRET_KEY should be set and should not randomly generate each time
# because it will invalidate all existing sessions
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "aF8NPVRZOlx5kC2hbcU7SivfskHXq8CESY8QcehsPe4="
)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

DEBUG=DEBUG,

SECRET_KEY=SECRET_KEY,

ROOT_URLCONF = "main.urls"

ALLOWED_HOSTS=ALLOWED_HOSTS,

MIDDLEWARE_CLASSES=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
],

INSTALLED_APPS=[
    "django.contrib.staticfiles",
]

TEMPLATE_DIRS = [
    BASE_DIR / "templates",
]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = "/static/"
