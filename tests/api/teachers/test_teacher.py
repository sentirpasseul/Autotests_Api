import random

import pytest
import requests

from services.general.models.error_response import ValidationError
from services.university.group.models.subjects import Subjects
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.assertions.general_assertions import Assertions
from conftest import generate_random_teacher
from utils.responses.general_responses import GeneralErrors
from utils.responses.user_responses import UserErrorsStrEnum


class TestTeacher:
    def test_get_teachers_status_code_success(self, teacher_helper):
        response = teacher_helper.get_teachers()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_teachers_response_success(self, university_service, soft_assert):
        created_teacher = university_service.create_teacher(generate_random_teacher())
        response = university_service.get_teachers()
        soft_assert.check(len(response.root) > 0, f"No any teachers have found")
        soft_assert.check(created_teacher.id in [teacher.id for teacher in response])
        soft_assert.assert_all()

    def test_get_teachers_without_token_response(self, university_api_utils_anonym):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.get_teachers()
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    def test_create_teacher_status_code_success(self, university_api_utils, teacher_helper):
        teacher = generate_random_teacher()
        response = teacher_helper.post_teacher(teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

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

    def test_create_teacher_without_token(self, university_api_utils_anonym):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.create_teacher(generate_random_teacher())
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    @pytest.mark.xfail
    def test_create_teacher_invalid_data(self, university_service):
        response = university_service.create_teacher(TeacherRequest(
            first_name='-',
            last_name='-',
            subject=random.choice(list(Subjects))
        ))
        assert isinstance(response, ValidationError)

    def test_delete_teacher(self, university_api_utils, teacher_helper, get_teacher_id):
        response = teacher_helper.delete_teacher(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_teacher_by_id(self, teacher_helper, university_api_utils, get_teacher_id):
        response = teacher_helper.get_teacher_by_id(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_teacher_by_id(self, teacher_helper, university_api_utils, get_teacher_id):
        teacher = generate_random_teacher()
        response = teacher_helper.put_teacher_by_id(teacher_id=get_teacher_id,
                                                    json=teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
