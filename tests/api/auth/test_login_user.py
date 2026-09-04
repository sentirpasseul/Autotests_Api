import requests.status_codes
from allure_commons.types import Severity

from services.authorization.authorization_service import AuthorizationService
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from utils.assertions.general_assertions import Assertions
from utils.responses.user_responses import UserErrorsStrEnum
from utils.logs.allure_conf.allure_config import allure_test_report
from utils.logs.allure_conf.allure_data import Feature, Epic, Story, Suit, SubSuit, ParentSuit, Label


class TestLoginUser:
    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.AUTH,
        epic=Epic.USER,
        feature=Feature.AUTH,
        story=Story.LOGIN_VALID,
        label=Label.POSITIVE,
        title="Login user got 200 ok",
        description="Verify that response's status code is 200 ok",
        severity=Severity.BLOCKER
    )
    def test_login_user_success(self, auth_api_utils_anonym, soft_assert, get_random_user):
        auth_helper = AuthorizationHelper(auth_api_utils_anonym)
        user = get_random_user
        auth_helper.post_register(data=user.model_dump())
        response = auth_helper.post_login(user.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.AUTH,
        epic=Epic.USER,
        feature=Feature.AUTH,
        story=Story.LOGIN_INVALID,
        title="Login with non-existed user",
        description="Verify that non-existed user can not login",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_login_user_invalid_creds(self, auth_api_utils_anonym, soft_assert, get_random_user):
        user = get_random_user
        auth_service = AuthorizationService(auth_api_utils_anonym)
        response = auth_service.login_user(login_request=LoginRequest(
            username=user.username,
            password=user.password
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_LOGIN_CREDENTIALS)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.AUTH,
        epic=Epic.USER,
        feature=Feature.AUTH,
        story=Story.LOGIN_INVALID,
        title="Test login with empty body",
        description="Verify that login with empty data respond correct error",
        severity=Severity.NORMAL,
        label=Label.NEGATIVE
    )
    def test_login_user_empty_body(self, auth_api_utils_anonym, soft_assert):
        auth_service = AuthorizationService(auth_api_utils_anonym)
        response = auth_service.login_user(login_request=LoginRequest(
            username='',
            password=''
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_LOGIN_CREDENTIALS)
