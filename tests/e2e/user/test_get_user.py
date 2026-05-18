from utils.assertions.user_assertions import UserAssertions

class TestGetUser:

    def test_get_user(self, generate_random_user, get_user_by_token):
        random_user = generate_random_user
        response = get_user_by_token
        UserAssertions.check_user_data(actual=random_user, expected=response)



