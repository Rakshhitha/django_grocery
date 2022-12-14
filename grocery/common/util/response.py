# from rest_framework import status
from rest_framework.response import Response
from common.message_en import (SUCCESS, INVALID_DATA)


def return_error_response(msg, code=400, status=False, data=None):
    return Response(
        {
            "message": msg,
            "code": code,
            "status": status,
            "success": False,
            "data": data
        }
    )


def response(status=True, code=200, message=SUCCESS, data=None, extra={}):
    response_data = {
        "status": status,
        "message": message,
        "code": code,
        **extra
    }
    if data is not None:
        response_data['data'] = data
    return Response(
        response_data
    )
