from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.login_response import LoginResponse
from services.authorization.models.register_request import RegisterRequest
from services.authorization.models.success_response import SuccessResponse
from services.authorization.user.helpers.user_helper import UserHelper
from services.authorization.user.models.user import UserResponse
from services.general.base_service import BaseService
from services.general.models.error_response import ErrorResponse, ValidationError
from utils.api_utils import ApiUtils


class AuthorizationService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.authorization_helpers = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(self, register_request: RegisterRequest):
        response = self.authorization_helpers.post_register(data=register_request.model_dump())
        if response == 201:
            return SuccessResponse(**response.json())
        if response == 409:
            return ErrorResponse(**response.json())
        if response == 422:
            return ValidationError(**response.json())



        return response

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authorization_helpers.post_login(data=login_request.model_dump())
        return LoginResponse(**response.json())

    def get_user_by_token(self) -> UserResponse:
        response = self.user_helper.get_me()
        return UserResponse(**response.json())
