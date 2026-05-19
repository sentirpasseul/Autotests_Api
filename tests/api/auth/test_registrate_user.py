import requests.status_codes

from services.authorization.helpers.authorization_helper import AuthorizationHelper
from utils.assertions.general_assertions import Assertions


class TestRegistrateUser:
    def test_registrate_user_success(self, auth_api_utils_anonym, generate_random_user, auth_helper):
        register_response = auth_helper.post_register(generate_random_user.model_dump())
        Assertions.validate_response_status_code(register_response, requests.codes.created)
