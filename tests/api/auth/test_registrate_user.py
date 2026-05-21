import pytest
import requests.status_codes
from utils.assertions.general_assertions import Assertions
from faker import Faker
from services.authorization.models.register_request import RegisterRequest
from utils.factories.factory_random_data import FactoryRandomData
from utils.responses.error_responses import UserErrorsStrEnum
from utils.responses.user_responses import UserResponsesStrEnum
import random


class TestRegistrateUser:
    ALLOWED_SPECIAL_CHARS = '!"#$%&\'()*+,-./:;<=>?@^_`{|}~[]'

    def test_registrate_user_success(self, auth_api_utils_anonym, generate_random_user, auth_helper,
                                     user_helper):
        response_register = auth_helper.post_register(generate_random_user.model_dump())
        Assertions.validate_response_status_code(response_register, requests.codes.created)
        assert response_register.json()['detail'] == UserResponsesStrEnum.USER_REGISTERED, \
            f"\n[FAIL] {response_register.request.method} {response_register.url} \n" \
            f"Actual: {response_register.json()['detail']} \n" \
            f"Expected: {UserResponsesStrEnum.USER_REGISTERED} \n"

    def test_registrate_user_duplicate_username(self, generate_random_user, auth_service):
        auth_service.register_user(generate_random_user)
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=generate_random_user.password,
            password_repeat=generate_random_user.password_repeat,
            email=Faker().email()
        ))
        Assertions.validate_response_status_code(response, requests.codes.conflict)
        assert response.json()['detail'] == UserErrorsStrEnum.USERNAME_IS_TAKEN, \
            f"\n[FAIL] {response.request.method} {response.url} \n" \
            f"Actual: {response.json()['detail']} \n" \
            f"Expected: {UserErrorsStrEnum.USERNAME_IS_TAKEN} \n"

    def test_registrate_user_duplicate_email(self, generate_random_user, auth_service):
        auth_service.register_user(generate_random_user)
        password = FactoryRandomData.generate_random_password()
        response = auth_service.register_user(RegisterRequest(
            username=Faker().user_name(),
            password=password,
            password_repeat=password,
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response, requests.codes.conflict)
        assert response.json()['detail'] == UserErrorsStrEnum.EMAIL_IS_TAKEN, \
            f"\n[FAIL] {response.request.method} {response.url} \n" \
            f"Actual: {response.json()['detail']} \n" \
            f"Expected: {UserErrorsStrEnum.EMAIL_IS_TAKEN} \n"

    def test_registrate_min_valid_password(self, generate_random_user, auth_service):
        password = (f'{random.choice(self.ALLOWED_SPECIAL_CHARS)}'
                    f'{Faker().random_digit_not_null()}'
                    f'{Faker().lexify(text='?' * 6)}')
        response_min_password = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response_min_password, requests.codes.created)

    def test_registrate_max_valid_password(self, generate_random_user, auth_service):
        password = (f'{random.choice(self.ALLOWED_SPECIAL_CHARS)}'
                    f'{Faker().random_digit_not_null()}'
                    f'{Faker().lexify(text='?' * 97)}')
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_registrate_password_min_boundary_failed(self, auth_service, generate_random_user):
        password = (f'{random.choice(self.ALLOWED_SPECIAL_CHARS)}'
                    f'{Faker().random_digit_not_null()}'
                    f'{Faker().lexify(text='?' * 5)}')
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_max_boundary_failed(self, auth_service, generate_random_user):
        password = (f'{random.choice(self.ALLOWED_SPECIAL_CHARS)}'
                    f'{Faker().random_digit_not_null()}'
                    f'{Faker().lexify(text='?' * 99)}')
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_empty_password(self, generate_random_user, auth_service):
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password='',
            password_repeat='',
            email=generate_random_user.email
        ))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    @pytest.mark.xfail
    def test_registrate_empty_username(self, generate_random_user, auth_service):
        response = auth_service.register_user(RegisterRequest(
            username='',
            password=generate_random_user.password,
            password_repeat=generate_random_user.password_repeat,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_passwords_not_match(self, generate_random_user, auth_service):
        password = FactoryRandomData.generate_random_password()
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=generate_random_user.password,
            password_repeat=password,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_without_special_chars(self, generate_random_user, auth_service):
        password = f'{Faker().lexify(text='?' * 8)}{Faker().random_digit_not_null()}'
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_without_number(self, generate_random_user, auth_service):
        password = f"{Faker().lexify(text='?' * 8)}{random.choice(self.ALLOWED_SPECIAL_CHARS)}"
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_only_letters(self, generate_random_user, auth_service):
        password = f"{Faker().lexify(text='?' * 10)}"
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_without_letters(self, generate_random_user, auth_service):
        password = f'{random.randrange(1000000, 9999999)}{random.choice(self.ALLOWED_SPECIAL_CHARS)}'
        response = auth_service.register_user(RegisterRequest(
            username=generate_random_user.username,
            password=password,
            password_repeat=password,
            email=generate_random_user.email))
        Assertions.validate_response_status_code(response, requests.codes.created)
