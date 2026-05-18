import random

import pytest

from services.authorization.authorization_service import AuthorizationService
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.register_request import RegisterRequest
from services.authorization.user.models.user import UserResponse
from services.university.grade.helpers.grade_helper import GradeHelper
from services.university.group.helpers.group_helper import GroupHelper
from services.university.group.models.group_request import GroupRequest
from services.university.student.helpers.student_helper import StudentHelper
from services.university.student.models.student import DegreeEnum
from services.university.student.models.student_request import StudentRequest
from services.university.teacher.helpers.teacher_helper import TeacherHelper
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker

from utils.logs.logger.logger import Logger

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthorizationService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils(access_token):
    api_utils = ApiUtils(url=AuthorizationService.SERVICE_URL,
                         token=access_token)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_helper(auth_api_utils_anonym):
    return AuthorizationHelper(api_utils=auth_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym(access_token):
    university_utils = ApiUtils(url=UniversityService.SERVICE_URL,
                                token=access_token)
    return university_utils


@pytest.fixture(scope="function", autouse=False)
def university_service(university_api_utils_anonym):
    university_service = UniversityService(university_api_utils_anonym)
    return university_service


@pytest.fixture(scope="function", autouse=False)
def student_helper(university_api_utils_anonym):
    return StudentHelper(api_utils=university_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def grade_helper(university_api_utils_anonym):
    return GradeHelper(api_utils=university_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def teacher_helper(university_api_utils_anonym):
    return TeacherHelper(api_utils=university_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def group_helper(university_api_utils_anonym):
    return GroupHelper(api_utils=university_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym, generate_random_user):
    auth_service = AuthorizationService(auth_api_utils_anonym)
    random_user = generate_random_user
    auth_service.register_user(register_request=random_user)
    login_response = auth_service.login_user(login_request=LoginRequest(username=random_user.username,
                                                                        password=random_user.password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def generate_random_user(auth_api_utils_anonym):
    username = faker.user_name()
    password_username = faker.password(length=30,
                                       special_chars=True,
                                       digits=True,
                                       upper_case=True,
                                       lower_case=True)
    email = faker.email()
    user_data = {
        "username": username,
        "password": password_username,
        "password_repeat": password_username,
        "email": email
    }
    log_data = user_data.copy()
    Logger.info(f"Generated user: {log_data}")
    return RegisterRequest(**user_data)


@pytest.fixture(scope="function", autouse=False)
def get_user_by_token(auth_api_utils, access_token):
    auth_service = AuthorizationService(auth_api_utils)
    user = auth_service.get_user_by_token()
    return UserResponse(**user.model_dump())


@pytest.fixture(scope="function", autouse=False)
def get_user_id(generate_random_user, auth_helper):
    user = generate_random_user
    user_id = auth_helper.post_register(user.model_dump()).json()['id']
    return user_id


@pytest.fixture(scope="function", autouse=False)
def generate_random_group(university_service):
    group = GroupRequest(name=faker.bothify("???-##-#"))
    Logger.info(f"Generated group: {group}")
    group_response = university_service.create_group(group_request=group)
    return group_response


@pytest.fixture(scope="function", autouse=False)
def generate_random_student(university_service, generate_random_group):
    student = StudentRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             email=faker.email(),
                             degree=random.choice([option for option in DegreeEnum]),
                             phone=faker.numerify("+7##########"), group_id=generate_random_group.id)
    Logger.info(f"Generated student: {student}")
    return student


@pytest.fixture(scope="function", autouse=False)
def get_student_id(university_api_utils_anonym, generate_random_student, student_helper):
    student = generate_random_student
    student_id = student_helper.post_student(student.model_dump()).json()['id']
    return student_id


@pytest.fixture(scope="function", autouse=False)
def generate_random_teacher(university_api_utils_anonym):
    teacher = {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "subject": faker.job()
    }
    Logger.info(f"Generated teacher: {teacher}")
    return TeacherRequest(**teacher)


@pytest.fixture(scope="function", autouse=False)
def get_group_id(university_api_utils_anonym, generate_random_group, group_helper):
    group = generate_random_group
    group_id = group_helper.get_group_by_id(group.id)
    return group_id


@pytest.fixture(scope="function", autouse=False)
def get_teacher_id(university_api_utils_anonym, generate_random_teacher, teacher_helper):
    teacher = generate_random_teacher
    teacher_id = teacher_helper.post_teacher(teacher.model_dump()).json()['id']
    return teacher_id
