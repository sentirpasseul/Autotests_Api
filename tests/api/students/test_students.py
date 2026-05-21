import requests.status_codes

from conftest import student_helper
from services.university.student.helpers.student_helper import StudentHelper
from utils.assertions.general_assertions import Assertions
from utils.factories.factory_random_data import FactoryRandomData


class TestStudents:
    def test_get_students(self, student_helper):
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_students_with_fake_token(self, student_helper_fake_token):
        response = student_helper_fake_token.get_students()
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_get_students_without_creds(self, student_api_utils_anonym):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_create_student(self, student_helper, generate_random_student):
        response = student_helper.post_student(generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_create_student_with_fake_token(self, student_helper_fake_token, generate_random_student):
        response = student_helper_fake_token.post_student(generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_create_student_without_creds(self, student_api_utils_anonym, generate_random_student):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.post_student(generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_delete_student(self, student_helper, get_student_id):
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_delete_student_without_creds(self, student_api_utils_anonym, get_student_id):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_get_student_by_id(self, student_helper, get_student_id):
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_get_student_by_id_without_creds(self, student_api_utils_anonym, student_helper, get_student_id):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_put_student_by_id(self, student_helper, get_student_id, generate_random_student):
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_student_with_fake_token(self, student_helper_fake_token, get_student_id, generate_random_student):
        response = student_helper_fake_token.put_student_by_id(student_id=get_student_id,
                                                               json=generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_put_student_by_id_without_creds(self, student_api_utils_anonym, student_helper, get_student_id,
                                             generate_random_student):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)
