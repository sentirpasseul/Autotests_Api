from http.client import responses

from services.general.base_service import BaseService
from services.university.group.models.group_request import GroupRequest
from services.university.group.models.group_response import GroupResponse
from services.university.group.helpers.group_helper import GroupHelper
from services.university.student.helpers.student_helper import StudentHelper
from services.university.student.models.student_request import StudentRequest
from services.university.student.models.student_response import StudentResponse
from utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def get_student(self, student_id: int):
        response = self.student_helper.get_student_by_id(student_id)
        return StudentResponse(**response.json())