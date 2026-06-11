import requests.status_codes

from conftest import student_helper, generate_random_student
from services.university.student.helpers.student_helper import StudentHelper
from utils.assertions.general_assertions import Assertions
from utils.responses.student_responses import StudentResponse


class TestStudents:
    def test_get_students_status_code(self, student_helper):
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_students_correct_response(self, university_service, soft_assert, get_group_id):
        student = university_service.create_student(generate_random_student(get_group_id))
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

    def test_get_students_with_fake_token(self, student_helper_fake_token):
        response = student_helper_fake_token.get_students()
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_get_students_without_creds(self, university_api_utils_anonym):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_create_student(self, student_helper, get_group_id):
        student = generate_random_student(get_group_id)
        response = student_helper.post_student(student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_create_student_with_fake_token(self, student_helper_fake_token, get_group_id):
        response = student_helper_fake_token.post_student(generate_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_create_student_without_creds(self, university_api_utils_anonym, get_group_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.post_student(generate_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_create_student_check_response(self, get_group_id, university_service, soft_assert):
        student = generate_random_student(get_group_id)
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

    def test_delete_student_status_code(self, student_helper, get_student_id):
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_student_response(self, university_service, get_student_id):
        response = university_service.delete_student(get_student_id)
        Assertions.validate_message(response, StudentResponse.STUDENT_DELETED)

    def test_delete_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_delete_student_without_creds(self, university_api_utils_anonym, get_student_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden or requests.codes.unauthorized)

    def test_get_student_by_id(self, student_helper, get_student_id):
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_student_with_fake_token(self, student_helper_fake_token, get_student_id):
        response = student_helper_fake_token.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_get_student_by_id_without_creds(self, university_api_utils_anonym, student_helper, get_student_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_put_student_by_id(self, student_helper, get_student_id, get_group_id):
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=generate_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_student_with_fake_token(self, student_helper_fake_token, get_student_id, get_group_id):
        response = student_helper_fake_token.put_student_by_id(student_id=get_student_id,
                                                               json=generate_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_put_student_by_id_without_creds(self, university_api_utils_anonym, student_helper, get_student_id,
                                             get_group_id):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=generate_random_student(get_group_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)
