from services.general.base_service import BaseService
from services.student.helpers.student_helper import StudentHelper
from utils.api_utils import ApiUtils


class StudentService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"
    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.student_helper = StudentHelper(api_utils)