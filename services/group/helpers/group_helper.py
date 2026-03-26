import requests

from services.general.helpers.base_helper import BaseHelper
from services.group.models.group_request import GroupRequest
from services.group.models.group_response import GroupResponse


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"

    def post_groups(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX, json=json)
        return response