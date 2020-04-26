from PIL import Image
from resizeimage import resizeimage
import sys

with open(sys.argv[1],'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image,[150,150])
        cover.save(sys.argv[2],image.format)

