from services.authorization.authorization_service import AuthorizationService
from utils.api_utils import ApiUtils
from utils.assertions.user_assertions import UserAssertions
from utils.responses.user_responses import UserResponsesStrEnum


class TestGetUser:

    def test_user(self, generate_random_user):
        auth_service = AuthorizationService(api_utils=ApiUtils(url=AuthorizationService.SERVICE_URL))
        register_user = auth_service.register_user(generate_random_user)
        assert register_user.json()['detail'] == UserResponsesStrEnum.USER_REGISTERED, \
            f"\n[FAIL] {register_user.request.method} {register_user.url} \n" \
            f"Actual: {register_user.json()['detail']} \n" \
            f"Expected: {register_user.USER_REGISTERED} \n"

        login = auth_service.login_user(generate_random_user)
        auth_service = AuthorizationService(api_utils=ApiUtils(
            url=AuthorizationService.SERVICE_URL,
            token=login.access_token))
        get_user = auth_service.get_user_by_token()
        UserAssertions.check_user_data(get_user, generate_random_user)




