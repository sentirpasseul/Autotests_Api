import random

import pytest

from services.authorization.authorization_service import AuthorizationService
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.models.login_request import LoginRequest
from services.authorization.models.register_request import RegisterRequest
from services.authorization.user.helpers.user_helper import UserHelper
from services.authorization.user.models.user import UserResponse
from services.university.grade.helpers.grade_helper import GradeHelper
from services.university.grade.models.grade import GradeRequest
from services.university.group.helpers.group_helper import GroupHelper
from services.university.group.models.group_request import GroupRequest
from services.university.group.models.subjects import Subjects
from services.university.student.helpers.student_helper import StudentHelper
from services.university.student.models.student import DegreeEnum
from services.university.student.models.student_request import StudentRequest
from services.university.teacher.helpers.teacher_helper import TeacherHelper
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from utils.assertions.soft_assert import SoftAssert

from utils.factories.factory_random_data import FactoryRandomData
from utils.logs.logger.logger import Logger


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthorizationService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_fake_token():
    token = FactoryRandomData.generate_jwt_token()
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, token=token)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def student_helper_fake_token(university_api_utils_fake_token):
    return StudentHelper(api_utils=university_api_utils_fake_token)


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils(access_token):
    api_utils = ApiUtils(url=AuthorizationService.SERVICE_URL,
                         token=access_token)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_helper(auth_api_utils_anonym):
    return AuthorizationHelper(api_utils=auth_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def user_helper(auth_api_utils_anonym):
    return UserHelper(api_utils=auth_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def university_api_utils(access_token):
    university_utils = ApiUtils(url=UniversityService.SERVICE_URL,
                                token=access_token)
    return university_utils


@pytest.fixture(scope="function", autouse=False)
def university_service(university_api_utils):
    university_service = UniversityService(university_api_utils)
    return university_service


@pytest.fixture(scope="function", autouse=False)
def auth_service(auth_api_utils_anonym):
    auth_service = AuthorizationService(auth_api_utils_anonym)
    return auth_service


@pytest.fixture(scope="function", autouse=False)
def student_helper(university_api_utils):
    return StudentHelper(api_utils=university_api_utils)


@pytest.fixture(scope="function", autouse=False)
def grade_helper(university_api_utils):
    return GradeHelper(api_utils=university_api_utils)


@pytest.fixture(scope="function", autouse=False)
def teacher_helper(university_api_utils):
    return TeacherHelper(api_utils=university_api_utils)


@pytest.fixture(scope="function", autouse=False)
def group_helper(university_api_utils):
    return GroupHelper(api_utils=university_api_utils)


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym, auth_service):
    user = generate_random_user()
    auth_service.register_user(register_request=user)
    login_response = auth_service.login_user(login_request=
    LoginRequest(
        username=user.username,
        password=user.password))
    return login_response.access_token


def generate_random_user():
    username = FactoryRandomData().faker.unique.user_name()
    password = FactoryRandomData.generate_random_password()
    email = FactoryRandomData().faker.unique.email()
    user_data = {
        "username": username,
        "password": password,
        "password_repeat": password,
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
def get_user_id(auth_api_utils_anonym, auth_service):
    user = generate_random_user()
    user_id = auth_service.register_user(user).id
    return user_id


def generate_random_group():
    group = GroupRequest(name=FactoryRandomData().faker.bothify("???-##-#"))
    Logger.info(f"Generated group: {group}")
    return group


def generate_random_student(group_id):
    student = StudentRequest(first_name=FactoryRandomData().faker.first_name(),
                             last_name=FactoryRandomData().faker.last_name(),
                             email=FactoryRandomData().faker.email(),
                             degree=random.choice([option for option in DegreeEnum]),
                             phone=FactoryRandomData().faker.numerify("+7##########"),
                             group_id=group_id)
    Logger.info(f"Generated student: {student}")
    return student


@pytest.fixture(scope="function", autouse=False)
def get_student_id(university_api_utils, university_service, get_group_id):
    student = generate_random_student(get_group_id)
    student_id = university_service.create_student(student).id
    return student_id


def generate_random_teacher():
    teacher = {
        "first_name": FactoryRandomData().faker.first_name(),
        "last_name": FactoryRandomData().faker.last_name(),
        "subject": random.choice(list(Subjects))
    }
    Logger.info(f"Generated teacher: {teacher}")
    return TeacherRequest(**teacher)


def generate_random_grade(teacher_id, student_id):
    grade = {
        "teacher_id": teacher_id,
        "student_id": student_id,
        "grade": FactoryRandomData.get_random_grade()
    }
    Logger.info(f"Generated grade: {grade}")
    return GradeRequest(**grade)


@pytest.fixture(scope="function", autouse=False)
def get_group_id(university_api_utils, university_service):
    group = generate_random_group()
    group_id = university_service.create_group(group).id
    return group_id


@pytest.fixture(scope="function", autouse=False)
def get_teacher_id(university_api_utils, university_service):
    teacher = generate_random_teacher()
    teacher_id = university_service.create_teacher(teacher).id
    return teacher_id


@pytest.fixture(scope="function", autouse=False)
def get_grade_id(university_api_utils, university_service, get_teacher_id, get_student_id):
    grade = generate_random_grade(teacher_id=get_teacher_id, student_id=get_student_id)
    grade_id = university_service.create_grade(grade).id
    return grade_id


@pytest.fixture(scope="function", autouse=False)
def soft_assert():
    sa = SoftAssert()
    yield sa
    sa.assert_all()
