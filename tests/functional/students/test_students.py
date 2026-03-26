import requests.status_codes

from services.student.helpers.student_helper import StudentHelper
from services.student.models.student_request import StudentsRequest


class TestStudents:
    def test_get_students(self, student_api_utils_anonym):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.get_students()
        student_helper.validate_response_status_code(response, requests.codes.ok)

    def test_create_student(self, student_api_utils_anonym, generate_random_student):
        student_helper = StudentHelper(api_utils=student_api_utils_anonym)
        response = student_helper.post_student({
            "first_name": generate_random_student["first_name"],
            "last_name": generate_random_student["last_name"],
            "email": generate_random_student["email"],
            "degree": generate_random_student["degree"],
            "phone": generate_random_student["phone"],
            "group_id": generate_random_student["group_id"]
        })

        student_helper.validate_response_status_code(response, requests.codes.created)
