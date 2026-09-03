import requests.status_codes
from allure_commons.types import Severity

from services.university.student.helpers.student_helper import StudentHelper
from utils.assertions.general_assertions import Assertions
from utils.responses.student_responses import StudentResponse
from utils.logs.allure_conf.allure_data import ParentSuit, Suit, SubSuit, Story, Feature, Label, Epic
from utils.logs.allure_conf.allure_config import allure_test_report


class TestStudents:
    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_VALID,
        feature=Feature.GET_STUDENTS,
        title="Get students - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_students_status_code(self, student_helper):
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_VALID,
        feature=Feature.GET_STUDENTS,
        title="Get students - correct message",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_students_correct_response(self, university_service, soft_assert, get_group_id, get_random_student):
        student = university_service.create_student(get_random_student(get_group_id))
        response = university_service.get_student(student.id)
        soft_assert.check(response.first_name == student.first_name,
                          message=f"First name mismatch: got {response.first_name}, expected {student.first_name}")
        soft_assert.check(response.last_name == student.last_name,
                          message=f"Last name mismatch: got {response.last_name}, expected {student.last_name}")
        soft_assert.check(response.email == student.email,
                          message=f"Email mismatch: got {response.email}, expected {student.email}")
        soft_assert.check(response.degree == student.degree,
                          message=f"Degree mismatch: got {response.degree}, expected {student.degree}")
        soft_assert.check(response.phone == student.phone,
                          message=f"Phone mismatch: got {response.phone}, expected {student.phone}")
        soft_assert.check(response.group_id == student.group_id,
                          message=f"Group id mismatch: got {response.group_id}, expected {student.group_id}")
        soft_assert.check(response.id == student.id,
                          message=f"Student id mismatch: got {response.id}, expected {student.id}")
        soft_assert.assert_all()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_INVALID,
        feature=Feature.GET_STUDENTS,
        title="Get students with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_get_students_with_fake_token(self, student_helper_fake_token):
        response = student_helper_fake_token.get_students()
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_INVALID,
        feature=Feature.GET_STUDENTS,
        title="Get students without credentials - status code (403) forbidden",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_get_students_without_creds(self, university_api_utils_anonym):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_STUDENT,
        title="Create student - status code 201 (created)",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_student(self, student_helper, get_group_id, get_random_student):
        student = get_random_student(get_group_id)
        response = student_helper.post_student(student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_STUDENT,
        title="Create student with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_student_with_fake_token(self, student_helper_fake_token, get_group_id, get_random_student):
        response = student_helper_fake_token.post_student(get_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_STUDENT,
        title="Create student without credentials - status code 403 (forbidden)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_student_without_creds(self, university_api_utils_anonym, get_group_id, get_random_student):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.post_student(get_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_STUDENT,
        title="Create student - correct data",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_student_check_response(self, get_group_id, university_service, soft_assert, get_random_student):
        student = get_random_student(get_group_id)
        response = university_service.create_student(student)
        soft_assert.check(response.first_name == student.first_name,
                          message=f"First name mismatch: got {response.first_name}, "
                                  f"expected {student.first_name}")
        soft_assert.check(response.last_name == student.last_name,
                          message=f"Last name mismatch: got {response.last_name}, "
                                  f"expected {student.last_name}")
        soft_assert.check(response.email == student.email,
                          message=f"Email mismatch: got {response.email}, "
                                  f"expected {student.email}")
        soft_assert.check(response.degree == student.degree,
                          message=f"Degree mismatch: got {response.degree}, "
                                  f"expected {student.degree}")
        soft_assert.check(response.phone == student.phone,
                          message=f"Phone mismatch: got {response.phone}, "
                                  f"expected {student.phone}")
        soft_assert.check(response.group_id == student.group_id,
                          message=f"Group id mismatch: got {response.group_id}, "
                                  f"expected {student.group_id}")
        soft_assert.assert_all()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.DELETE_VALID,
        feature=Feature.DELETE_STUDENT,
        title="Delete student - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_student_status_code(self, student_helper, get_student_id):
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.DELETE_VALID,
        feature=Feature.DELETE_STUDENT,
        title="Delete student - check valid message",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_delete_student_response(self, university_service, get_student_id):
        response = university_service.delete_student(get_student_id)
        Assertions.validate_message(response, StudentResponse.STUDENT_DELETED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_STUDENT,
        title="Delete student with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.LOGIN_INVALID,
        feature=Feature.DELETE_STUDENT,
        title="Delete student without credentials - status code 401/403",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_student_without_creds(self, university_api_utils_anonym, get_student_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden or requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_VALID,
        feature=Feature.GET_STUDENT,
        title="Get student by student_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_student_by_id(self, student_helper, get_student_id):
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_INVALID,
        feature=Feature.GET_STUDENT,
        title="Get student with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_get_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.GET_VALID,
        feature=Feature.GET_STUDENT,
        title="Get student by student_id without credentials - status code 403 (forbidden)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_get_student_by_id_without_creds(self, university_api_utils_anonym, student_helper, get_student_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.UPDATE_PUT_VALID,
        feature=Feature.UPDATE_PUT_STUDENT,
        title="Update (put) student by student_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_put_student_by_id(self, student_helper, get_student_id, get_group_id, get_random_student):
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=get_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.UPDATE_PUT_INVALID,
        feature=Feature.UPDATE_PUT_STUDENT,
        title="Update (put) student by student_id with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_put_student_with_fake_token(self, student_helper_fake_token, get_student_id, get_group_id,
                                         get_random_student):
        response = student_helper_fake_token.put_student_by_id(student_id=get_student_id,
                                                               json=get_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.STUDENTS,
        epic=Epic.STUDENTS,
        story=Story.UPDATE_PUT_INVALID,
        feature=Feature.UPDATE_PUT_STUDENT,
        title="Update (put) student by student_id without credentials - status code 403 (forbidden)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_put_student_by_id_without_creds(self, university_api_utils_anonym, student_helper, get_student_id,
                                             get_group_id, get_random_student):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=get_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)
