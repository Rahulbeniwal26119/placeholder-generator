from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag

from main.utils import generate_etag
from main.forms import ImageForm


def index(request):
    return HttpResponse("Hello World")

@etag(generate_etag)
def placeholder(request, width, height):
    watermark = request.GET.get("watermark", True)
    form = ImageForm({"height": height, "width": width, "watermark": watermark})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type="image/png")
    else:
        return HttpResponseBadRequest("Invalid Image Request")
