import os
import logging
import uuid
import re
import random

from django.conf import settings
from django.core.signing import TimestampSigner
from django.db import connections

from common.constants import EMAIL_REGEX
from django.core.mail import EmailMultiAlternatives

from datetime import datetime
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_email_verified)
    
generate_token = TokenGenerator()

    

def jwt_payload_handler(user):
    """ Custom payload handler
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    return {
        'user_id': user.pk,
        'user_name': user.username,
        # 'email': user.email,
        # 'mobile_number': user.mobile_number,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }

def get_time_stamp_signer():
    return TimestampSigner()


def represent_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_random_alphanumeric(string_length=10):
    random_number = str(uuid.uuid4()).upper().replace("-", "")[0:string_length]
    return random_number


def get_random_number():
    random_number = random.randint(100000, 999999)
    return random_number


def generate_otp():
    random_number = random.randint(1000, 9999)
    return random_number


def generate_confirmation_token(email):
    signer = get_time_stamp_signer()
    value = signer.sign(email)
    return value


def confirm_token(token, expiration=settings.EMAIL_LINK_EXPIRE_TIME):
    signer = get_time_stamp_signer()
    try:
        email = signer.unsign(token, max_age=expiration)
    except:
        return False

    return email


def find_email_or_phone(input_field):
    import re
    email_regex = re.compile(
        r"""(
            [a-zA-Z0-9._%+-]+           # username
            @                           # @ symbol
            [a-zA-Z0-9.-]+              # domain name
            (\.[a-zA-Z]{2,4})           # dot something
        )""",
        re.VERBOSE,
    )
    phone_dash_regex = re.compile(
        r"""(
            (\d{3}|\(\d{3}\))?          # area code
            (\s|-|\.)?                  # separator
            \d{3}                       # first 3 digits
            (\s|-|\.)                   # separator
            \d{4}                       # last 4 digits
            (\s*(ext|x|ext.)\s*\d{2,5})?# extension
        )""",
        re.VERBOSE,
    )
    phone_regex = re.compile(
        r"""(^[1-9](\d)+$)""",
        re.VERBOSE,
    )
    email_found = re.match(email_regex, input_field)
    phone_found = re.match(phone_regex, input_field)
    if email_found:
        return email_found.group(), "email"
    elif phone_found:
        return phone_found.group(), "phone"
    else:
        return None, None


def generate_html_message_body(subject, message_body):
    message_object = {
        "Subject": {
            "Data": subject
        },
        "Body": {
            "Html": {
                "Data": message_body
            }
        }
    }
    return message_object


def get_unique_name():
    return uuid.uuid4().hex


def get_file_extension(filename):
    filename, file_extension = os.path.splitext(filename)
    return file_extension


def validate_foreign_key(model, fk):
    try:
        model.objects.get(id=fk)
        return fk
    except Exception:
        from rest_framework import serializers
        raise serializers.ValidationError(F"{model.__name__} doesn't exist")


def is_email_valid(email):
    return bool(email and re.match(EMAIL_REGEX, email))


def generate_template(password, email, template_type='CREATE_PASSWORD', link=None):

    if template_type == "FORGOT_PASSWORD":

        template_body = F"Hello {email}<br><br>"\
                        F"<a href={password}>Click here to change your "\
                        F"password</a> <br><br>"\
                        F"If the link above does not work, paste this into your browser:"\
                        F"<br>{password} <br><br>"\
                        F"If you do not wish to change your password, please disregard "\
                        F"this message. <br><br>"\

        return template_body
    elif template_type == "PASSWORD_RESET":
        template_body = F"Hello!<br><br>"\
                        F"We have resetted password for your email<br><br>"\
                        F"Email is {email}  <br><br>"\
                        F"Password is {password} <br><br>"
        return template_body
    elif template_type == "EMAIL_VERIFICATION":
        template_body = F"Hello!<br><br>"\
                        F"Please verify your email address<br><br>"\
                        F"Email is {email}  <br><br>"\
                        F"Verification link is <a href={link}>link</a>"
        return template_body
    elif template_type == "EMAIL_VERIFIED":
        template_body = F"Hello!<br><br>"\
                        F"Your email address is been verified<br><br>"\
                        F"Email is {email}  <br><br>"
        return template_body

    return ""


def check_dirs(_path, mode=0o777, exist_ok=True):
    if not os.path.exists(_path):
        os.makedirs(_path, mode=mode, exist_ok=exist_ok)


def send_email_verification(email, data, template_type, email_subject):
    message = generate_template('', email, template_type, data['link'])
    msg = EmailMultiAlternatives(subject=email_subject, body=message,
                                 from_email="admin@repro.com",
                                 to=[email])
    msg.attach_alternative(message, "text/html")
    msg.send()
    log.info(msg)


def send_email_verified(email, data, template_type, email_subject):
    message = generate_template('', email, template_type, [])
    msg = EmailMultiAlternatives(subject=email_subject, body=message,
                                 from_email="admin@repro.com",
                                 to=[email])
    msg.attach_alternative(message, "text/html")
    msg.send()


# Raw Query service using cursor with SQLquery, replacements and multiple rows flag as
# parameters


def raw_query(sql, replacements, many):
    with connections.cursor() as cursor:
        cursor.execute(
            "SET sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));")
        cursor.execute(sql, replacements)
        if many:
            data = cursor.fetchall()
            columns = [x[0] for x in cursor.description]
            log.info(cursor._executed)
            return [
                dict(zip(columns, row))
                for row in data
            ]
        columns = (x[0] for x in cursor.description)
        log.info(cursor._executed)
        query_data = cursor.fetchone()
        return dict(zip(columns, query_data))

