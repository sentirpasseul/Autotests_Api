import requests.status_codes

from services.authorization.authorization_service import AuthorizationService
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.register_request import RegisterRequest
from utils.logs.logger.logger import Logger


class TestRegistrateUser:
    def test_registrate_user_success(self, auth_api_utils_anonym, generate_random_user):
        authorization_helper = AuthorizationHelper(api_utils=auth_api_utils_anonym)
        register_response =  authorization_helper.post_register({
            "username": generate_random_user["username"],
            "password": generate_random_user["password"],
            "password_repeat": generate_random_user["password"],
            "email": generate_random_user["email"]
        })
        authorization_helper.validate_response_status_code(register_response, requests.codes.created)
        #register_response.text


