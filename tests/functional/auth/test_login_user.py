import requests.status_codes

from services.authorization.helpers.authorization_helper import AuthorizationHelper
from utils.api_utils import ApiUtils


class TestLoginUser:
    def test_login_user_success(self, auth_api_utils_anonym):
        authorization_helper = AuthorizationHelper(api_utils=auth_api_utils_anonym)
        response = authorization_helper.post_login({
            "username": "allenmark",
            "password": "MZoq23Hs0GyG3lbvt*4XmeHi^c(rFV"
        })
        authorization_helper.validate_response_status_code(response, requests.codes.ok)
        #{'username': 'allenmark', 'password': 'MZoq23Hs0GyG3lbvt*4XmeHi^c(rFV', 'email': 'jennifer19@example.org'}