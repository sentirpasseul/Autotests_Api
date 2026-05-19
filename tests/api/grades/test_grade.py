import requests

from utils.assertions.general_assertions import Assertions


class TestGrade:

    def test_create_grade(self, grade_helper, get_student_id, get_teacher_id, get_random_grade):
        response = grade_helper.post_grade(data={
            "teacher_id": get_teacher_id,
            "student_id": get_student_id,
            "grade": get_random_grade
        })
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_get_grades_with_params(self, grade_helper, get_student_id, get_teacher_id, get_group_id):
        response = grade_helper.get_grades(data={
            "student_id": get_student_id,
            "teacher_id": get_teacher_id,
            "group_id": get_group_id})
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_grades_without_params(self, grade_helper):
        response = grade_helper.get_grades()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_grade_by_id(self, grade_helper, get_grade_id):
        response = grade_helper.delete_grade(get_grade_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_grade_by_id(self, grade_helper, get_grade_id, generate_random_grade):
        response = grade_helper.put_grade_by_id(grade_id=get_grade_id,
                                                data=generate_random_grade.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_stat(self, grade_helper, get_student_id, get_group_id, get_teacher_id):
        response = grade_helper.get_grades_stat(data={
                "group_id": get_group_id,
                "student_id": get_student_id,
                "teacher_id": get_teacher_id})
        Assertions.validate_response_status_code(response, requests.codes.ok)
