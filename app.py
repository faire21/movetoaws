from PIL import Image
from resizeimage import resizeimage
import sys
import boto3
import io

#Open up aws 
s3 = boto3.client('s3')
s3r = boto3.resource('s3')
bucket = 'practica2buck'

#New name for the new file
filename = 'SMALL'+sys.argv[1]

#Download the file with the new name
s3.download_file(bucket, sys.argv[1], filename)
print('image downloaded')

#Open downloaded file and resize image
with Image.open(filename) as image:
    cover = resizeimage.resize_cover(image,[150,150])

#Convert Pil image to a file that aws can store
memfile = io.BytesIO()
cover.save(memfile, format = cover.format)
memfile.seek(0)

#AWS PUT
s3r.Bucket(bucket).put_object(Key=filename, Body=memfile)
