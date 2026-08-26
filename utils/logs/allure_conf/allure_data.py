from enum import StrEnum


class Suit(StrEnum):
    SMOKE = "Smoke"
    REGRESS = "Regression"


class SubSuit(StrEnum):
    AUTH = "Authorization"
    REGISTER = "Registration"

class ParentSuit(StrEnum):
    API = "API Tests"


class Epic(StrEnum):
    USER = "User Management"


class Feature(StrEnum):
    AUTH = "Authorization"
    REGISTER = "Registration"


class Story(StrEnum):
    LOGIN_VALID = "Login user with valid data"
    LOGIN_INVALID = "Login user with invalid data"

    REGISTER_VALID = "Register user with valid data"
    REGISTER_INVALID = "Register user with invalid data"
