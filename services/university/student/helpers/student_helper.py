import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    STUDENT_ID_ENDPOINT = f"{ENDPOINT_PREFIX}/{{student_id}}"

    def get_students(self) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_PREFIX)
        return response

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX, json=json)
        return response

    def delete_student(self, student_id: int) -> requests.Response:
        response = self.api_utils.delete(self.STUDENT_ID_ENDPOINT.format(student_id=student_id))
        return response

    def get_student_by_id(self, student_id: int) -> requests.Response:
        response = self.api_utils.get(self.STUDENT_ID_ENDPOINT.format(student_id=student_id))
        return response

    def put_student_by_id(self, student_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.STUDENT_ID_ENDPOINT.format(student_id=student_id), json=json)
        return response
