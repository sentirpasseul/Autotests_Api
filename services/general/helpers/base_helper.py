import requests

from utils.api_utils import ApiUtils


class BaseHelper:
    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    @staticmethod
    def validate_response_status_code(response: requests.Response, expected_code: int):
        assert response.status_code == expected_code, \
            f"\n[FAIL] {response.request.method} {response.url}" \
            f"Actual: {response.status_code} \n" \
            f"Expected: {expected_code} \n"
