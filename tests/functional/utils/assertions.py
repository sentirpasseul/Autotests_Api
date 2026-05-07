import requests


class Assertions:

    @staticmethod
    def validate_response_status_code(response: requests.Response, expected_code: int):
        assert response.status_code == expected_code, \
            f"\n[FAIL] {response.request.method} {response.url}" \
            f"Actual: {response.status_code} \n" \
            f"Expected: {expected_code} \n"
