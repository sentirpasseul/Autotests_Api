import requests.status_codes

from services.authorization.helpers.authorization_helper import AuthorizationHelper
from utils.assertions.general_assertions import Assertions


class TestLoginUser:
    def test_login_user_success(self, auth_api_utils, generate_random_user):
        auth_helper = AuthorizationHelper(auth_api_utils)
        response = auth_helper.post_login(generate_random_user.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
