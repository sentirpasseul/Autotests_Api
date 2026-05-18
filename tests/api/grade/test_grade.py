import requests

from utils.assertions.general_assertions import Assertions

class TestGrade:

    def test_get_stat(self, grade_helper, get_student_id, get_group_id, get_teacher_id):
        response = grade_helper.get_grades_stat(group_id=get_group_id,
                                     student_id=get_student_id,
                                     teacher_id=get_teacher_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)