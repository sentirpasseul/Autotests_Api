from enum import StrEnum


class UserErrorsStrEnum(StrEnum):
    USERNAME_IS_TAKEN = "Username is already taken"
    EMAIL_IS_TAKEN = "Email is already taken"
    INVALID_LOGIN_CREDENTIALS = "Invalid login credentials"
    ACCESS_DENIED = "Access denied"

class UserResponsesStrEnum(StrEnum):
    USER_REGISTERED = "User registered"

class AuthErrorsStrEnum(StrEnum):
    MISMATCH_BODY_RESPONSE = "Mismatch body response"

    PASSWORD_MIN_LEN_ERROR = "Value error, Password length should be longer than 7 characters"
    PASSWORD_MAX_LEN_ERROR = "Value error, Password length should be shorter than 100 characters"
    PASSWORD_SPECIAL_CHAR = "Value error, Password must contains at least one special character"
    PASSWORDS_MISMATCH = "Value error, Passwords do not match"
    PASSWORD_DIGIT_ERROR = "Value error, Password must contains at least one digit"