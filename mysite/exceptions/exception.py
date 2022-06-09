from rest_framework.exceptions import APIException

# TODO: TMI
class Error400(APIException):
    status_code = 400
    default_detail = '400 Error'

# TODO: TMI
class Error404(APIException):
    status_code = 404
    default_detail = '404 Error'

# TODO: TMI
class Error500(APIException):
    status_code = 500
    default_detail = '500 Error'