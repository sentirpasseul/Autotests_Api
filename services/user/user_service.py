from services.general.base_service import BaseService
from services.user.helpers.user_helper import UserHelper
from utils.api_utils import ApiUtils


class UserService(BaseService):
    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def get_user_me(self):
        self.user_helper.get_me()