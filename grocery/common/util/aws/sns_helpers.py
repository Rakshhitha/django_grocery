import boto3
import os
import requests
from decouple import config
from common.util.logger import get_custom_logger

log = get_custom_logger()
# Using Amazon s3
client = boto3.client('s3')

BUCKET_NAME = ''

S3_URL = 'https://s3-ap-southeast-1.amazonaws.com'
S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY') or config('S3_ACCESS_KEY')
S3_SECRET_KEY = os.environ.get('S3_SECRET_KEY') or config('S3_SECRET_KEY')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME') or config('S3_BUCKET_NAME')

client = boto3.client(
    "sns",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name="ap-south-1"
)


def send_mobile_otp(number, otp):
    """Sends an OTP to the 'number' value

    Parameters
    ----------
    number: integer
        The mobile number to which the OTP is to be sent
    otp: integer
        The otp which is sent to the mobile number
    """
    res = client.publish(
        PhoneNumber=number,
        Message="Your OTP is: {}".format(otp),
    )

    log.info(res)

    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 1
    else:
        return 0