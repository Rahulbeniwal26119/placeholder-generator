from io import BytesIO
from django import forms
from django.core.cache import cache

from PIL import Image, ImageDraw, ImageFont
from cairosvg import svg2png
from main.utils import get_default_placeholder_svg


class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=3000)
    width = forms.IntegerField(min_value=1, max_value=3000)
    watermark = forms.CharField(required=False, max_length=5)

    def generate(self, image_format="PNG"):
        height = self.cleaned_data["height"]
        width = self.cleaned_data["width"]
        watermark = self.cleaned_data["watermark"]

        key = f"{width}.{height}.{watermark}.{image_format}"
        content = cache.get(key)
        svg = get_default_placeholder_svg()

        if content is None:
            output_file = BytesIO()
            content = BytesIO()

            svg2png(
                bytestring=svg,
                write_to=output_file,
                parent_height=height,
                parent_width=width,
                dpi=96,
                scale=1,
                output_width=width,
                output_height=height,
            )

            output_file.seek(0)

            image = Image.open(output_file)
            draw = ImageDraw.Draw(image)
            text = f"{width}x{height}"

            if watermark:
                font_width, font_height = height * 0.05, width * 0.05
                font_size = int(min(font_width, font_height))
                font = ImageFont.load_default(size=font_size)

                draw.text((0, 0), text, fill=(100, 100, 100), font=font)

            image.save(content, image_format)
            content.seek(0)

            cache.set(key, content, 60 * 60)

        return content

    def clean_watermark(self):
        watermark = self.cleaned_data["watermark"]
        if watermark in ["false", "0"]:
            return False
        else:
            return True
