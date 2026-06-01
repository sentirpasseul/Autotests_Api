import requests

from conftest import generate_random_student, generate_random_teacher, generate_random_grade, generate_random_group
from services.university.grade.models.grade import GradeRequest, GradeStatRequest
from utils.assertions.general_assertions import Assertions
from utils.factories.factory_random_data import FactoryRandomData


class TestGrade:

    def test_create_grade_status_code(self, grade_helper, get_student_id, get_teacher_id):
        response = grade_helper.post_grade(data={
            "teacher_id": get_teacher_id,
            "student_id": get_student_id,
            "grade": FactoryRandomData().get_random_grade()
        })
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_create_grade_check_response(self, university_service, soft_assert,
                                         get_group_id, get_teacher_id, get_student_id):
        grade = FactoryRandomData.get_random_grade()
        response = university_service.create_grade(GradeRequest(teacher_id=get_teacher_id,
                                                                student_id=get_student_id,
                                                                grade=grade))
        soft_assert.check(response.teacher_id == get_teacher_id,
                          message=f"Teacher id mismatch: got {response.teacher_id}, expected {get_teacher_id}")
        soft_assert.check(response.student_id == get_student_id,
                          message=f"Student id mismatch: got {response.student_id}, expected {get_student_id}")
        soft_assert.check(response.grade == grade,
                          message=f"Grade mismatch: got {response.grade}, expected {grade}")
        soft_assert.assert_all()

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

    def test_put_grade_by_id(self, grade_helper, get_grade_id, get_teacher_id, get_student_id):
        response = grade_helper.put_grade_by_id(grade_id=get_grade_id,
                                                data=generate_random_grade(student_id=get_student_id,
                                                                           teacher_id=get_teacher_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_stat(self, grade_helper, get_student_id, get_group_id, get_teacher_id):
        response = grade_helper.get_grades_stat(data={
            "group_id": get_group_id,
            "student_id": get_student_id,
            "teacher_id": get_teacher_id})
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_stat_check_response(self, university_service, soft_assert, get_group_id):
        student = university_service.create_student(generate_random_student(get_group_id))
        teacher = university_service.create_teacher(generate_random_teacher())
        group = university_service.create_group(generate_random_group())
        response = university_service.get_stat(GradeStatRequest(student_id=student.id,
                                                                teacher_id=teacher.id,
                                                                group_id=group.id))
        #soft_assert.check(response)




