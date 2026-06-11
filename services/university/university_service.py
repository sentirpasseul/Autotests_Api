from services.general.models.error_response import ValidationError, ErrorResponse
from services.general.models.success_response import SuccessResponse
from services.general.base_service import BaseService
from services.university.grade.helpers.grade_helper import GradeHelper
from services.university.grade.models.grade import GradeCreateResponse, GradeRequest, GradeStatRequest, \
    GradeStatResponse, GradeUpdateResponse
from services.university.group.models.group_request import GroupRequest
from services.university.group.models.group_response import GroupResponse
from services.university.group.helpers.group_helper import GroupHelper
from services.university.student.helpers.student_helper import StudentHelper
from services.university.student.models.student_request import StudentRequest
from services.university.student.models.student_response import StudentResponse
from services.university.teacher.helpers.teacher_helper import TeacherHelper
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.teacher.models.teacher_response import TeacherResponse, TeachersResponse
from utils.api_utils import ApiUtils
import requests


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest):
        response = self.group_helper.post_group(json=group_request.model_dump())
        if response.status_code == requests.codes.created:
            return GroupResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def delete_group(self, group_id: int):
        response = self.group_helper.delete_group_by_id(group_id)
        if response.status_code == requests.codes.ok:
            return SuccessResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def create_student(self, student_request: StudentRequest):
        response = self.student_helper.post_student(json=student_request.model_dump())
        if response.status_code == requests.codes.created:
            return StudentResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest):
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        if response.status_code == requests.codes.created:
            return TeacherResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def get_teachers(self):
        response = self.teacher_helper.get_teachers()
        if response.status_code == requests.codes.ok:
            return TeachersResponse.model_validate(response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest):
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        if response.status_code == requests.codes.created:
            return GradeCreateResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def delete_grade(self, grade_id: int):
        response = self.grade_helper.delete_grade(grade_id)
        if response.status_code == requests.codes.ok:
            return SuccessResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def get_student(self, student_id: int):
        response = self.student_helper.get_student_by_id(student_id)
        if response.status_code == requests.codes.ok:
            return StudentResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def delete_student(self, student_id: int):
        response = self.student_helper.delete_student(student_id)
        if response.status_code == requests.codes.ok or response.status_code == requests.codes.created:
            return SuccessResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def get_stat(self, grade_stat_request: GradeStatRequest):
        response = self.grade_helper.get_grades_stat(data=grade_stat_request.model_dump())
        if response.status_code == requests.codes.ok:
            return GradeStatResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def put_grade_by_id(self, grade_id: int, grade_request: GradeRequest):
        response = self.grade_helper.put_grade_by_id(grade_id=grade_id, data=grade_request.model_dump())
        if response.status_code == requests.codes.ok:
            return GradeUpdateResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())

    def get_group_by_id(self, group_id: int):
        response = self.group_helper.get_group_by_id(group_id)
        if response.status_code == requests.codes.ok:
            return GroupResponse(**response.json())
        if response.status_code == requests.codes.unprocessable:
            return ValidationError(**response.json())
        else:
            return ErrorResponse(**response.json())
