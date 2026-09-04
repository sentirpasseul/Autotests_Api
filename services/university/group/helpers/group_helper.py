from http.client import responses

import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"
    GROUP_ID = f"{ENDPOINT_PREFIX}/{{group_id}}"

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT_PREFIX, json=json)
        return response

    def get_groups(self) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_PREFIX)
        return response

    def delete_group_by_id(self, group_id: int) -> requests.Response:
        response = self.api_utils.delete(self.GROUP_ID.format(group_id=group_id))
        return response

    def get_group_by_id(self, group_id: int) -> requests.Response:
        response = self.api_utils.get(self.GROUP_ID.format(group_id=group_id))
        return response

    def put_group_by_id(self, group_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.GROUP_ID.format(group_id=group_id), json=json)
        return response
