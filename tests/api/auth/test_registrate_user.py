import pytest
import requests.status_codes
from allure_commons.types import Severity

from utils.assertions.general_assertions import Assertions
from faker import Faker
from services.authorization.models.register_request import RegisterRequest
from utils.factories.factory_random_data import FactoryRandomData
from utils.logs.allure_conf.allure_config import allure_test_report
from utils.responses.user_responses import AuthErrorsStrEnum
from utils.responses.user_responses import UserErrorsStrEnum
from utils.responses.user_responses import UserResponsesStrEnum
import random
from utils.logs.allure_conf.allure_data import Epic, Story, Feature, Suit, SubSuit, ParentSuit, Label


class TestRegistrateUser:
    MIN_CHARS = 8

    faker = Faker()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user returns 201 Created",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_registrate_user_success_status_code(self, auth_api_utils_anonym,
                                                 auth_helper, user_helper, get_random_user):
        response_register = auth_helper.post_register(get_random_user.model_dump())
        Assertions.validate_response_status_code(response_register, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user with correct response body",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_registrate_user_success_response_body(self, auth_service, get_random_user):
        response = auth_service.register_user(get_random_user)
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with duplicate username - status code 409 (conflict)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_user_duplicate_username_status_code(self, auth_helper, get_random_user):
        user = get_random_user
        auth_helper.post_register(user.model_dump())
        user_data = {
            "username": user.username,
            "password": user.password,
            "password_repeat": user.password_repeat,
            "email": self.faker.email()
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with duplicate username - correct response error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    @pytest.mark.xfail
    def test_registrate_user_duplicate_username_response_body(self, auth_service, get_random_user):
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=user.password,
            password_repeat=user.password_repeat,
            email=self.faker.email()
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.USERNAME_IS_TAKEN)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with duplicate email - status code 409 (conflict)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_user_duplicate_email_status_code(self, auth_helper, get_random_user, get_random_password):
        user = get_random_user
        auth_helper.post_register(user.model_dump())
        password = get_random_password
        user_data = {
            "username": self.faker.user_name(),
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with duplicate email - correct response error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    @pytest.mark.xfail
    def test_registrate_user_duplicate_email_response_body(self, auth_service, get_random_user, get_random_password):
        user = get_random_user
        auth_service.register_user(user)
        password = get_random_password
        response = auth_service.register_user(RegisterRequest(
            username=self.faker.user_name(),
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.EMAIL_IS_TAKEN)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user with min valid password - status code 201 (created)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_registrate_min_valid_password_status_code(self, auth_helper, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 6)}')
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user with valid password - correct response message",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_registrate_min_valid_password_response_body(self, auth_service, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 6)}')
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user with max valid password - status code 201 (created)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_registrate_max_valid_password_status_code(self, auth_helper, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 97)}')
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_VALID,
        title="Register user with max valid password - correct response message",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_registrate_max_valid_password_response_body(self, auth_service, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 97)}')
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with min boundary password - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_min_boundary_failed_status_code(self, auth_helper, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 5)}')
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        epic=Epic.USER,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with min boundary password - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_min_boundary_failed_response_body(self, auth_service, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 5)}')
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_MIN_LEN_ERROR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with max boundary password - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_max_boundary_failed_status_code(self, auth_helper, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 99)}')
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with max boundary password - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_max_boundary_failed_response_body(self, auth_service, get_random_user):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 99)}')
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_MAX_LEN_ERROR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with empty password - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_empty_password_status_code(self, auth_helper, get_random_user):
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": '',
            "password_repeat": '',
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with empty password - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_empty_password_response_body(self, auth_service, get_random_user):
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password='',
            password_repeat='',
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with empty username - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    @pytest.mark.xfail
    def test_registrate_empty_username_status_code(self, auth_helper, get_random_user):
        user = get_random_user
        user_data = {
            "username": '',
            "password": user.password,
            "password_repeat": user.password_repeat,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with empty username - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )

    @pytest.mark.xfail
    def test_registrate_empty_username_response_body(self, auth_service, get_random_user):
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username='',
            password=user.password,
            password_repeat=user.password_repeat,
            email=user.email))
        Assertions.validate_message(response, UserErrorsStrEnum.EMAIL_INCORRECT)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with passwords not match - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_passwords_not_match_status_code(self, auth_helper, get_random_password, get_random_user):
        password = get_random_password
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": user.password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with passwords not match - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_passwords_not_match_response_body(self, auth_service, get_random_user, get_random_password):
        user = get_random_user
        password = get_random_password
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=user.password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORDS_MISMATCH)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without special chars - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_special_chars_status_code(self, auth_helper, get_random_user):
        password = f'{Faker().lexify(text='?' * self.MIN_CHARS)}{Faker().random_digit_not_null()}'
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without special chars - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_special_chars_response_body(self, auth_service, get_random_user):
        password = f'{Faker().lexify(text='?' * self.MIN_CHARS)}{Faker().random_digit_not_null()}'
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without number - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_number_status_code(self, auth_helper, get_random_user):
        password = f"{Faker().lexify(text='?' * self.MIN_CHARS)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}"
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without number - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_number_response_body(self, auth_service, get_random_user):
        password = f"{Faker().lexify(text='?' * self.MIN_CHARS)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}"
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_DIGIT_ERROR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password only letter - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_only_letters_status_code(self, auth_helper, get_random_user):
        password = f"{Faker().lexify(text='?' * 10)}"
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password only letters - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_only_letters_response_body(self, auth_service, get_random_user):
        password = f"{Faker().lexify(text='?' * 10)}"
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without letters - status code 422 (unprocessable)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_letters_status_code(self, auth_helper, get_random_user):
        password = f'{random.randrange(1000000, 9999999)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
        user = get_random_user
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.REGISTER,
        epic=Epic.USER,
        feature=Feature.REGISTER,
        story=Story.REGISTER_INVALID,
        title="Register user with password without letters - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_registrate_password_without_letters_response_body(self, auth_service, get_random_user):
        password = f'{random.randrange(1000000, 9999999)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
        user = get_random_user
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)
