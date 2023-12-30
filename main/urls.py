from django.urls import re_path as url
from main.views import index, placeholder

urlpatterns = [
    url(r"^$", index),
    url(
        r"^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$",
        placeholder,
        name="placeholder",
    ),
]