from rest_framework.exceptions import APIException


class Error400(APIException):
    status_code = 400
    default_detail = '400 Error'


class Error404(APIException):
    status_code = 404
    default_detail = '404 Error'


class Error500(APIException):
    status_code = 500
    default_detail = '500 Error'