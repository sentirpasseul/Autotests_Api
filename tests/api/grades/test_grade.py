import pytest
import requests

from conftest import generate_random_student, generate_random_teacher, generate_random_grade, generate_random_group
from services.university.grade.helpers.grade_helper import GradeHelper
from services.university.grade.models.grade import GradeRequest, GradeStatRequest
from utils.assertions.general_assertions import Assertions
from utils.factories.factory_random_data import FactoryRandomData
from utils.responses.grade_responses import GradeResponse, GradeErrorResponses


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

    def test_get_grades_with_params_status_code(self, grade_helper, get_student_id, get_teacher_id,
                                                get_group_id):
        response = grade_helper.get_grades(data={
            "student_id": get_student_id,
            "teacher_id": get_teacher_id,
            "group_id": get_group_id})
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_grades_without_params_status_code(self, grade_helper):
        response = grade_helper.get_grades()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_grade_by_id_status_code(self, grade_helper, get_grade_id):
        response = grade_helper.delete_grade(get_grade_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_grade_by_id_response(self, university_service, get_grade_id):
        response = university_service.delete_grade(get_grade_id)
        Assertions.validate_message(response, GradeResponse.GRADE_DELETED)

    def test_delete_not_active_grade_status_code(self, grade_helper, get_grade_id):
        grade_helper.delete_grade(get_grade_id)
        response = grade_helper.delete_grade(get_grade_id)
        Assertions.validate_response_status_code(response, requests.codes.not_found)

    def test_delete_not_active_grade_response(self, university_service, get_grade_id):
        university_service.delete_grade(get_grade_id)
        response = university_service.delete_grade(get_grade_id)
        Assertions.validate_message(response, GradeErrorResponses.GRADE_NOT_FOUND)

    def test_put_grade_by_id_status_code(self, grade_helper, get_grade_id, get_teacher_id, get_student_id):
        response = grade_helper.put_grade_by_id(grade_id=get_grade_id,
                                                data=generate_random_grade(student_id=get_student_id,
                                                                           teacher_id=get_teacher_id).model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_grade_by_id_response(self, university_service, grade_helper, get_grade_id, get_teacher_id,
                                      get_student_id, soft_assert):
        grade = FactoryRandomData.get_random_grade()
        response = university_service.put_grade_by_id(grade_id=get_grade_id,
                                                      grade_request=GradeRequest(
                                                          student_id=get_student_id,
                                                          teacher_id=get_teacher_id,
                                                          grade=grade
                                                      ))
        soft_assert.check(response.teacher_id == get_teacher_id,
                          f'Teacher id mismatch: got {response.teacher_id}, expected {get_teacher_id}')
        soft_assert.check(response.student_id == get_student_id,
                          f'Student id mismatch: got {response.student_id}, expected {get_student_id}')
        soft_assert.check(response.grade == grade,
                          f'Grade mismatch: got {response.grade}, expected {grade}')
        soft_assert.assert_all()

    def test_get_stat(self, grade_helper, get_student_id, get_group_id, get_teacher_id):
        response = grade_helper.get_grades_stat(data={
            "group_id": get_group_id,
            "student_id": get_student_id,
            "teacher_id": get_teacher_id})
        Assertions.validate_response_status_code(response, requests.codes.ok)


