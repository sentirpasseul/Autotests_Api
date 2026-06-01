import pytest
import requests.status_codes
from utils.assertions.general_assertions import Assertions
from faker import Faker
from services.authorization.models.register_request import RegisterRequest
from utils.responses.user_responses import AuthErrorsStrEnum
from utils.factories.factory_random_data import FactoryRandomData
from utils.responses.user_responses import UserErrorsStrEnum
from utils.responses.user_responses import UserResponsesStrEnum
import random
from conftest import generate_random_user


class TestRegistrateUser:
    MIN_CHARS = 8

    faker = Faker()

    def test_registrate_user_success_status_code(self, auth_api_utils_anonym,
                                                 auth_helper, user_helper):
        response_register = auth_helper.post_register(generate_random_user().model_dump())
        Assertions.validate_response_status_code(response_register, requests.codes.created)

    def test_registrate_user_success_response_body(self, auth_service):
        response = auth_service.register_user(generate_random_user())
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    def test_registrate_user_duplicate_username_status_code(self, auth_helper):
        user = generate_random_user()
        auth_helper.post_register(user.model_dump())
        user_data = {
            "username": user.username,
            "password": user.password,
            "password_repeat": user.password_repeat,
            "email": self.faker.email()
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    @pytest.mark.xfail
    def test_registrate_user_duplicate_username_response_body(self, auth_service):
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=user.password,
            password_repeat=user.password_repeat,
            email=self.faker.email()
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.USERNAME_IS_TAKEN)

    def test_registrate_user_duplicate_email_status_code(self, auth_helper):
        user = generate_random_user()
        auth_helper.post_register(user.model_dump())
        password = FactoryRandomData.generate_random_password()
        user_data = {
            "username": self.faker.user_name(),
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    def test_registrate_user_duplicate_email_response_body(self, auth_service):
        user = generate_random_user()
        auth_service.register_user(user)
        password = FactoryRandomData.generate_random_password()
        response = auth_service.register_user(RegisterRequest(
            username=self.faker.user_name(),
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserErrorsStrEnum.EMAIL_IS_TAKEN)

    def test_registrate_min_valid_password_status_code(self, auth_helper):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 6)}')
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_registrate_min_valid_password_response_body(self, auth_service):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 6)}')
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    def test_registrate_max_valid_password_status_code(self, auth_helper):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 97)}')
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_registrate_max_valid_password_response_body(self, auth_service):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 97)}')
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)

    def test_registrate_password_min_boundary_failed_status_code(self, auth_helper):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 5)}')
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_min_boundary_failed_response_body(self, auth_service):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 5)}')
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_MIN_LEN_ERROR)

    def test_registrate_password_max_boundary_failed_status_code(self, auth_helper):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 99)}')
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_max_boundary_failed_response_body(self, auth_service):
        password = (f'{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
                    f'{self.faker.random_digit_not_null()}'
                    f'{self.faker.lexify(text='?' * 99)}')
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_MAX_LEN_ERROR)

    def test_registrate_empty_password_status_code(self, auth_helper):
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": '',
            "password_repeat": '',
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_empty_password_response_body(self, auth_service):
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password='',
            password_repeat='',
            email=user.email
        ))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    @pytest.mark.xfail
    def test_registrate_empty_username_status_code(self, auth_helper):
        user = generate_random_user()
        user_data = {
            "username": '',
            "password": user.password,
            "password_repeat": user.password_repeat,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_message(response, requests.codes.unprocessable)

    @pytest.mark.skip
    def test_registrate_empty_username_response_body(self, auth_service):
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username='',
            password=user.password,
            password_repeat=user.password_repeat,
            email=user.email))
        Assertions.validate_message(response, '')

    def test_registrate_passwords_not_match_status_code(self, auth_helper):
        password = FactoryRandomData.generate_random_password()
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": user.password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_passwords_not_match_response_body(self, auth_service):
        user = generate_random_user()
        password = FactoryRandomData.generate_random_password()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=user.password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORDS_MISMATCH)

    def test_registrate_password_without_special_chars_status_code(self, auth_helper):
        password = f'{Faker().lexify(text='?' * self.MIN_CHARS)}{Faker().random_digit_not_null()}'
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_without_special_chars_response_body(self, auth_service):
        password = f'{Faker().lexify(text='?' * self.MIN_CHARS)}{Faker().random_digit_not_null()}'
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    def test_registrate_password_without_number_status_code(self, auth_helper):
        password = f"{Faker().lexify(text='?' * self.MIN_CHARS)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}"
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_without_number_response_body(self, auth_service):
        password = f"{Faker().lexify(text='?' * self.MIN_CHARS)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}"
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_DIGIT_ERROR)

    def test_registrate_password_only_letters_status_code(self, auth_helper):
        password = f"{Faker().lexify(text='?' * 10)}"
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.unprocessable)

    def test_registrate_password_only_letters_response_body(self, auth_service):
        password = f"{Faker().lexify(text='?' * 10)}"
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, AuthErrorsStrEnum.PASSWORD_SPECIAL_CHAR)

    def test_registrate_password_without_letters_status_code(self, auth_helper):
        password = f'{random.randrange(1000000, 9999999)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
        user = generate_random_user()
        user_data = {
            "username": user.username,
            "password": password,
            "password_repeat": password,
            "email": user.email
        }
        response = auth_helper.post_register(user_data)
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_registrate_password_without_letters_response_body(self, auth_service):
        password = f'{random.randrange(1000000, 9999999)}{random.choice(FactoryRandomData.ALLOWED_SPECIAL_CHARS)}'
        user = generate_random_user()
        response = auth_service.register_user(RegisterRequest(
            username=user.username,
            password=password,
            password_repeat=password,
            email=user.email))
        Assertions.validate_message(response, UserResponsesStrEnum.USER_REGISTERED)
