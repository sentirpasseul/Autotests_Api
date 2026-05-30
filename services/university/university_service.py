from services.general.models.error_response import ValidationError, ErrorResponse
from services.general.models.success_response import SuccessResponse
from services.general.base_service import BaseService
from services.university.grade.helpers.grade_helper import GradeHelper
from services.university.grade.models.grade import GradeResponse, GradeRequest
from services.university.group.models.group_request import GroupRequest
from services.university.group.models.group_response import GroupResponse
from services.university.group.helpers.group_helper import GroupHelper
from services.university.student.helpers.student_helper import StudentHelper
from services.university.student.models.student_request import StudentRequest
from services.university.student.models.student_response import StudentResponse
from services.university.teacher.helpers.teacher_helper import TeacherHelper
from services.university.teacher.models.teacher_request import TeacherRequest
from services.university.teacher.models.teacher_response import TeacherResponse
from utils.api_utils import ApiUtils
from utils.responses.handlers import handle_response_university


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grade_helper = GradeHelper(self.api_utils)


    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def get_student(self, student_id: int):
        response = self.student_helper.get_student_by_id(student_id)
        return StudentResponse(**response.json())

    @handle_response_university
    def delete_student(self, student_id: int):
        response = self.student_helper.delete_student(student_id)
        return response
