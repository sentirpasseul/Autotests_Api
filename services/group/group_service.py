from services.general.base_service import BaseService
from services.group.helpers.group_helper import GroupHelper
from services.group.models.group_request import GroupRequest
from services.group.models.group_response import GroupResponse
from utils.api_utils import ApiUtils


class GroupService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_groups(json=group_request.model_dump())
        return GroupResponse(**response.json())