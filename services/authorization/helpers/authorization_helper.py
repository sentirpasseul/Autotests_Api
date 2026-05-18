import requests

from services.general.helpers.base_helper import BaseHelper


class AuthorizationHelper(BaseHelper):
    ENDPOINT_PREFIX = "/auth"
    REGISTER_ENDPOINT = "/register/"
    LOGIN_ENDPOINT = "/login"

    def post_register(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX + self.REGISTER_ENDPOINT, data)
        return response

    def post_login(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX + self.LOGIN_ENDPOINT, data)
        return response
