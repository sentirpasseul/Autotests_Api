from utils.assertions.user_assertions import UserAssertions

class TestGetUser:

    def test_get_user(self, generate_random_user, get_user_by_token):
        response = get_user_by_token
        UserAssertions.check_user_data(actual=generate_random_user, expected=response)



