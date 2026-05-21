from enum import StrEnum


class UserErrorsStrEnum(StrEnum):
    USERNAME_IS_TAKEN = "Username is already taken"
    EMAIL_IS_TAKEN = "Email is already taken"
    INVALID_LOGIN_CREDENTIALS = "Invalid login credentials"
    ACCESS_DENIED = "Access denied"
