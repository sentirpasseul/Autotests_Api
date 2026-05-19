from services.general.helpers.base_helper import BaseHelper
import requests

class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = "/teachers"
    TEACHER_ID = ENDPOINT_PREFIX + "/{teacher_id}/"

    def get_teachers(self) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_PREFIX)
        return response

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(self.TEACHER_ID.format(teacher_id=teacher_id))
        return response

    def get_teacher_by_id(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.get(self.TEACHER_ID.format(teacher_id=teacher_id))
        return response

    def put_teacher_by_id(self, teacher_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.TEACHER_ID.format(teacher_id=teacher_id), json=json)
        return response