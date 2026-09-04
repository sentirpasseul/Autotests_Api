import requests

from services.general.models.success_response import SuccessResponse
from services.general.models.error_response import ErrorResponse, ValidationError
from utils.responses.general_responses import GeneralErrors


class Assertions:

    @staticmethod
    def validate_response_status_code(response: requests.Response, expected_code: int):
        assert response.status_code == expected_code, \
            f"\n[FAIL] {response.request.method} {response.url} \n" \
            f"Actual: {response.status_code} \n" \
            f"Expected: {expected_code} \n"

    @staticmethod
    def validate_message(response: ErrorResponse | ValidationError | SuccessResponse, message: str):
        if isinstance(response, ValidationError):
            assert response.detail[0].msg == message, \
                f"\n {GeneralErrors.PASSWORD_MIN_LEN_ERROR} \n" \
                f"Actual: {response.detail[0].msg} \n" \
                f"Expected: {message} \n"
        else:
            assert response.detail == message, \
                f"\n {GeneralErrors.MISMATCH_BODY_RESPONSE} \n" \
                f"Actual: {response.detail} \n" \
                f"Expected: {message} \n"
