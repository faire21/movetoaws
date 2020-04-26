from PIL import Image
from resizeimage import resizeimage
import sys
import boto3
import io

with open(sys.argv[1],'r+b') as f:
    filename = 'SMALL'+f.name
    s3 = boto3.client('s3')
    s3r = boto3.resource('s3')
    bucket = 'practica2buck'
    s3.download_file(bucket, f.name, filename)
    print('image downloaded')

with Image.open(filename) as image:
    cover = resizeimage.resize_cover(image,[150,150])

memfile = io.BytesIO()
cover.save(memfile, format = cover.format)

memfile.seek(0)

s3r.Bucket(bucket).put_object(Key=filename, Body=memfile)
