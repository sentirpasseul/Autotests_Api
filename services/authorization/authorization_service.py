from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.login_response import LoginResponse
from services.authorization.models.register_request import RegisterRequest
from services.authorization.models.success_response import SuccessResponse
from services.general.base_service import BaseService
from utils.api_utils import ApiUtils


class AuthorizationService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.authorization_helpers = AuthorizationHelper(self.api_utils)

    def register_user(self, register_request: RegisterRequest) -> SuccessResponse:
        response = self.authorization_helpers.post_register(data=register_request.model_dump())
        return SuccessResponse(**response.json())

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authorization_helpers.post_login(data=login_request.model_dump())
        return LoginResponse(**response.json())
