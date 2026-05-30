from functools import wraps
import requests
from services.general.models.error_response import ValidationError, ErrorResponse
from services.general.models.success_response import SuccessResponse


def handle_response_university(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == requests.codes.ok or response.status_code == requests.codes.created:
            return SuccessResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    return wrapper