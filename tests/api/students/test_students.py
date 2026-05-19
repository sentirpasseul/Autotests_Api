import requests.status_codes

from utils.assertions.general_assertions import Assertions


class TestStudents:
    def test_get_students(self, student_helper, university_api_utils_anonym):
        response = student_helper.get_students()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_create_student(self, university_api_utils_anonym, student_helper, generate_random_student):
        response = student_helper.post_student(generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_delete_student(self, student_helper, university_api_utils_anonym, get_student_id):
        response = student_helper.delete_student(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_student_by_id(self, student_helper, university_api_utils_anonym, get_student_id):
        response = student_helper.get_student_by_id(get_student_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_student_by_id(self, student_helper, university_api_utils_anonym, get_student_id,
                               generate_random_student):
        response = student_helper.put_student_by_id(student_id=get_student_id,
                                                    json=generate_random_student.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

