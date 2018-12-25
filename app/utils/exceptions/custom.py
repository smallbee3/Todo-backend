from rest_framework.exceptions import APIException

__all__ = (
    'CustomAPIException',
)


class CustomAPIException(APIException):
    detail = 'Invalid input'
    default_code = 'Invalid'

    def __init__(self, status_code=None, detail=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = detail
