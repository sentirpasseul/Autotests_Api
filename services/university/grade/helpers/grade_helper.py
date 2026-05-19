from services.general.helpers.base_helper import BaseHelper
import requests


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    GRADE_ID = ENDPOINT_PREFIX + "/{grade_id}"
    STATS = ENDPOINT_PREFIX + "/stats"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX, data=data)
        return response

    def get_grades(self, data: dict = None) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_PREFIX, data=data)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        response = self.api_utils.delete(self.GRADE_ID.format(grade_id=grade_id))
        return response

    def put_grade_by_id(self, grade_id: int, data: dict) -> requests.Response:
        response = self.api_utils.put(self.GRADE_ID.format(grade_id=grade_id), data=data)
        return response

    def get_grades_stat(self, data: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS, data=data)
        return response
