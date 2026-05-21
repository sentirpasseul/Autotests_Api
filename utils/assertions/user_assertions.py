from services.authorization.models.register_request import RegisterRequest
from services.authorization.user.models.user import UserResponse


class UserAssertions:
    @staticmethod
    def check_user_data(actual: UserResponse, expected: RegisterRequest):
        assert actual.username == expected.username, \
        f"Username mismatch: got {actual.username}, expected {expected.username}"
        assert actual.email == expected.email, \
        f"Email mismatch: got {actual.email}, expected {expected.email}"
        assert actual.is_enabled is True, \
        f"User enabled mismatch: got {expected.is_enabled}, expected {True}"