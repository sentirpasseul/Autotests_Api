import random

import pytest
import requests
from allure_commons.types import Severity

from services.general.models.error_response import ValidationError
from services.university.group.models.subjects import Subjects
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.assertions.general_assertions import Assertions
from conftest import generate_random_teacher
from utils.responses.user_responses import UserErrorsStrEnum
from utils.logs.allure_conf.allure_data import ParentSuit, Suit, SubSuit, Story, Feature, Label, Epic
from utils.logs.allure_conf.allure_config import allure_test_report


class TestTeacher:
    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.GET_VALID,
        feature=Feature.GET_TEACHERS,
        title="Get teachers - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_teachers_status_code_success(self, teacher_helper):
        response = teacher_helper.get_teachers()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.GET_VALID,
        feature=Feature.GET_TEACHERS,
        title="Get teachers - check response",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_teachers_response_success(self, university_service, soft_assert):
        created_teacher = university_service.create_teacher(generate_random_teacher())
        response = university_service.get_teachers()
        soft_assert.check(len(response.root) > 0, f"No any teachers have found")
        soft_assert.check(created_teacher.id in [teacher.id for teacher in response])
        soft_assert.assert_all()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.GET_INVALID,
        feature=Feature.GET_TEACHERS,
        title="Get teachers without token - check correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_get_teachers_without_token_response(self, university_api_utils_anonym):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.get_teachers()
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_TEACHER,
        title="Create teacher - status code 201 (created)",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_teacher_status_code_success(self, university_api_utils, teacher_helper):
        teacher = generate_random_teacher()
        response = teacher_helper.post_teacher(teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_TEACHER,
        title="Create teacher - check response",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_teacher_response_success(self, university_service, soft_assert):
        teacher = generate_random_teacher()
        response = university_service.create_teacher(teacher)
        soft_assert.check(teacher.first_name == response.first_name,
                          f"Teacher's firstname mismatch: got {response.first_name}, expected {teacher.first_name}")
        soft_assert.check(teacher.last_name == response.last_name,
                          f"Teacher's lastname mismatch: got {response.last_name}, expected {teacher.last_name}")
        soft_assert.check(teacher.subject == response.subject,
                          f"Teacher's subject mismatch: got {response.subject}, expected {teacher.subject}")
        soft_assert.assert_all()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_TEACHER,
        title="Create teacher without token - check error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_teacher_without_token(self, university_api_utils_anonym):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.create_teacher(generate_random_teacher())
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_TEACHER,
        title="Create teacher with invalid data in body - check error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    @pytest.mark.xfail
    def test_create_teacher_invalid_data(self, university_service):
        response = university_service.create_teacher(TeacherRequest(
            first_name='-',
            last_name='-',
            subject=random.choice(list(Subjects))
        ))
        assert isinstance(response, ValidationError)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.DELETE_VALID,
        feature=Feature.DELETE_TEACHER,
        title="Delete teacher - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_delete_teacher(self, university_api_utils, teacher_helper, get_teacher_id):
        response = teacher_helper.delete_teacher(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.GET_VALID,
        feature=Feature.GET_TEACHER,
        title="Get teacher by teacher_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_teacher_by_id(self, teacher_helper, university_api_utils, get_teacher_id):
        response = teacher_helper.get_teacher_by_id(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.TEACHERS,
        epic=Epic.TEACHERS,
        story=Story.UPDATE_PUT_VALID,
        feature=Feature.UPDATE_PUT_TEACHER,
        title="Update (put) teacher by teacher_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_put_teacher_by_id(self, teacher_helper, university_api_utils, get_teacher_id):
        teacher = generate_random_teacher()
        response = teacher_helper.put_teacher_by_id(teacher_id=get_teacher_id,
                                                    json=teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
