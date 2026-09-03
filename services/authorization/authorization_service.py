from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.login_response import LoginResponse
from services.authorization.models.register_request import RegisterRequest
from services.general.models.success_response import SuccessResponse
from services.authorization.user.helpers.user_helper import UserHelper
from services.authorization.user.models.user import UserResponse
from services.general.base_service import BaseService
from services.general.models.error_response import ErrorResponse, ValidationError
from utils.api_utils import ApiUtils
import requests


class AuthorizationService(BaseService):
    SERVICE_URL = "http://host.docker.internal:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.authorization_helpers = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(self, register_request: RegisterRequest):
        response = self.authorization_helpers.post_register(data=register_request.model_dump())
        if response.status_code == requests.codes.created:
            return SuccessResponse(**response.json())
        if response.status_code != requests.codes.unprocessable:
            return ErrorResponse(**response.json())
        else:
            return ValidationError(**response.json())

    def login_user(self, login_request: LoginRequest):
        response = self.authorization_helpers.post_login(data=login_request.model_dump())
        if response.status_code == requests.codes.ok:
            return LoginResponse(**response.json())
        if response.status_code != requests.codes.unprocessable:
            return ErrorResponse(**response.json())
        else:
            return ValidationError(**response.json())

    def get_user_by_token(self):
        response = self.user_helper.get_me()
        if response.status_code == requests.codes.created:
            return UserResponse(**response.json())
        if response.status_code != requests.codes.unprocessable:
            return ErrorResponse(**response.json())
        else:
            return ValidationError(**response.json())

