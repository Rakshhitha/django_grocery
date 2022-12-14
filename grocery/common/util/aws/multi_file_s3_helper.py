import boto3
import os
import random
import string
import zipfile

from decouple import config

# Using Amazon s3
client = boto3.client('s3')

BUCKET_NAME = ''

S3_URL = 's3-website.ap-south-1.amazonaws.com'
S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY') or config('S3_ACCESS_KEY')
S3_SECRET_KEY = os.environ.get('S3_SECRET_KEY') or config('S3_SECRET_KEY')
# S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME') or config('S3_BUCKET_NAME')
S3_BUCKET_NAME = ''

client = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)


def multifile_upload(random_name, dir_name):
    chars = string.ascii_uppercase + string.digits
    randomName = ''.join(random.choice(chars) for _ in range(8))
    tmpFolder = '/tmp/' + random_name + '/'
    os.makedirs(tmpFolder)
    unzipTmpFile = random_name + '.zip'
    attachmentFolder = ''
    extension = ".zip"
    targetDirectory = "random_name"
    for item in os.listdir(tmpFolder):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(dir_name)
            zip_ref.close()
            os.remove(file_name)

    mrssFiles = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(tmpFolder):
        for file in f:
            mrssFiles.append(os.path.join(r, file))
    for file_name in mrssFiles:
        client.upload_file(file_name, S3_BUCKET_NAME, targetDirectory +
                           '/' + file_name.replace(tmpFolder, '', 1))
        os.remove(file_name)
    return {
        'data': "https://" + S3_BUCKET_NAME + S3_URL + random_name
    }
