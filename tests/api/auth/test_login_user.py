import requests.status_codes
from conftest import generate_random_user
from services.authorization.authorization_service import AuthorizationService
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from utils.assertions.general_assertions import Assertions


class TestLoginUser:
    def test_login_user_success(self, auth_api_utils_anonym):
        auth_helper = AuthorizationHelper(auth_api_utils_anonym)
        user = generate_random_user()
        auth_helper.post_register(data=user.model_dump())
        response = auth_helper.post_login(user.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_login_user_success_response(self, auth_api_utils_anonym):
        user = generate_random_user()
        auth_service = AuthorizationService(auth_api_utils_anonym)
        auth_service.register_user(user)
        response = auth_service.login_user(login_request=LoginRequest(
            username=user.username,
            password=user.password
        ))
