from enum import StrEnum


class GeneralErrors(StrEnum):
    MISMATCH_BODY_RESPONSE = "Mismatch body response"
    PASSWORD_MIN_LEN_ERROR = "Value error, Password length should be longer than 7 characters"
    PASSWORD_MAX_LEN_ERROR = "Value error, Password length should be shorter than 100 characters"
    PASSWORD_SPECIAL_CHAR = "Value error, Password must contains at least one special character"
