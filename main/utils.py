import hashlib
from django.http import HttpRequest
from django.core.cache import cache
from django.conf import settings


def generate_etag(request: HttpRequest, width: int, height: int) -> str:
    watermark = request.GET.get("watermark", "true")
    content = f"Placeholder: {width}x{height} {watermark}"
    return hashlib.sha1(content.encode("utf-8")).hexdigest()


def get_default_placeholder_svg():
    default_placeholder_key = "default_placeholder_svg"
    if cache.get(default_placeholder_key) is None:
        file = settings.STATICFILES_DIRS[0] / "default.svg"
        content = open(file, "r").read()
        cache.set(default_placeholder_key, content, 60 * 60)
    return cache.get(default_placeholder_key)
