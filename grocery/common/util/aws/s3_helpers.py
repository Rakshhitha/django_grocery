import boto3
import os

from decouple import config

# Using Amazon s3
client = boto3.client('s3')

BUCKET_NAME = ''

S3_URL = 'https://s3-ap-south-1.amazonaws.com'
S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY') or config('S3_ACCESS_KEY')
S3_SECRET_KEY = os.environ.get('S3_SECRET_KEY') or config('S3_SECRET_KEY')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME') or config('S3_BUCKET_NAME')

client = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)


# Upload a file
def upload_file(file, key):
    client.upload_file(file, BUCKET_NAME, key)
    image_url = F'{S3_URL}/{BUCKET_NAME}/{key}'
    return image_url


# Upload a file obj
def upload_file_obj(file_obj, key):
    with open(file_obj, 'rb') as data:
        client.upload_fileobj(data, BUCKET_NAME, key)
        image_url = F'{S3_URL}/{BUCKET_NAME}/{key}'
        return image_url


# Download an S3 object to a file.
def download_s3_file(file_name, key):
    client.Object(BUCKET_NAME, key).download_file(file_name)
