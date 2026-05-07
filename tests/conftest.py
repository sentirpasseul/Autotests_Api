import random

import pytest

from services.authorization.authorization_service import AuthorizationService
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.register_request import RegisterRequest
from services.group.group_service import GroupService
from services.group.models.group_request import GroupRequest
from services.student.helpers.student_helper import StudentHelper
from services.student.models.student import DegreeEnum
from services.student.models.student_request import StudentRequest
from services.student.student_service import StudentService
from utils.api_utils import ApiUtils
from faker import Faker

from utils.logs.logger.logger import Logger

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthorizationService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    pass


@pytest.fixture(scope="function", autouse=False)
def group_api_utils_anonym(access_token):
    api_utils = ApiUtils(url=GroupService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def student_api_utils_anonym(access_token):
    api_utils = ApiUtils(url=StudentService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils

@pytest.fixture(scope="function", autouse=False)
def student_helper(student_api_utils_anonym):
    return StudentHelper(api_utils=student_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym, generate_random_user):
    auth_service = AuthorizationService(auth_api_utils_anonym)

    auth_service.register_user(register_request=RegisterRequest(username=generate_random_user["username"],
                                                                password=generate_random_user["password"],
                                                                password_repeat=generate_random_user["password"],
                                                                email=generate_random_user["email"]))
    login_response = auth_service.login_user(login_request=LoginRequest(username=generate_random_user["username"],
                                                                        password=generate_random_user["password"]))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def generate_random_user():
    user_data = {
        "username": faker.user_name(),
        "password": faker.password(length=30,
                                   special_chars=True,
                                   digits=True,
                                   upper_case=True,
                                   lower_case=True),
        "email": faker.email()
    }
    log_data = user_data.copy()
    Logger.info(f"Generated user: {log_data}")
    return user_data


@pytest.fixture(scope="function", autouse=False)
def generate_random_group(group_api_utils_anonym):
    group_service = GroupService(group_api_utils_anonym)
    group = GroupRequest(name=faker.bothify("???-##-#"))
    group_response = group_service.create_group(group_request=group)
    return group_response


@pytest.fixture(scope="function", autouse=False)
def generate_random_student(group_api_utils_anonym, generate_random_group):
    student = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "degree": random.choice([option for option in DegreeEnum]),
        "phone": faker.numerify("+7##########"),
        "group_id": generate_random_group.id
    }
    Logger.info(f"Generated student: {student}")
    return student


@pytest.fixture(scope="function", autouse=False)
def get_student_id(student_api_utils_anonym, generate_random_student):
    student_helper = StudentHelper(student_api_utils_anonym)
    student = StudentRequest(**generate_random_student)
    student_id = student_helper.post_student(student.model_dump()).json()['id']
    return  student_id


@pytest.fixture(scope="function", autouse=False)
def set_headers():
    pass
