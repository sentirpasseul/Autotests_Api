import requests

from utils.assertions.general_assertions import Assertions
from conftest import generate_random_teacher


class TestTeacher:
    def test_get_teachers(self, university_api_utils_anonym, teacher_helper):
        response = teacher_helper.get_teachers()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_create_teacher(self, university_api_utils_anonym, teacher_helper):
        teacher = generate_random_teacher()
        response = teacher_helper.post_teacher(teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_delete_teacher(self, university_api_utils_anonym, teacher_helper, get_teacher_id):
        response = teacher_helper.delete_teacher(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_teacher_by_id(self, teacher_helper, university_api_utils_anonym, get_teacher_id):
        response = teacher_helper.get_teacher_by_id(get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_teacher_by_id(self, teacher_helper, university_api_utils_anonym, get_teacher_id):
        teacher = generate_random_teacher()
        response = teacher_helper.put_teacher_by_id(teacher_id=get_teacher_id,
                                                    json=teacher.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
