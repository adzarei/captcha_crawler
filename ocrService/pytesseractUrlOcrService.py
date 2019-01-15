import pytesseract
import requests
from PIL import ImageFilter
from PIL import Image
from io import BytesIO


# Filter and enhance image lettering.
def process_image(url):
    image = _get_image(url)
    image - filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


# Retrive image form URL
def _get_image(url):
    return Image.open(BytesIO(requests.get(url).content))
