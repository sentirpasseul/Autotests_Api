from enum import StrEnum


class Suit(StrEnum):
    SMOKE = "Smoke"
    REGRESS = "Regression"


class SubSuit(StrEnum):
    AUTH = "Authorization"
    REGISTER = "Registration"
    GRADE = "Grades"
    GROUPS = "Groups"
    TEACHERS = "Teachers"
    STUDENTS = "Students"

class ParentSuit(StrEnum):
    API = "API Tests"


class Epic(StrEnum):
    USER = "User Management"
    GRADE = "Grades Managements"


class Feature(StrEnum):
    AUTH = "Authorization"
    REGISTER = "Registration"

    CREATE_GRADE = "Create grade"
    GET_GRADES = "Get grade"
    DELETE_GRADE = "Delete grade"

    UPGRADE_GRADE_PUT = "Upgrade grade (put)"

    GET_STAT = "Get statistics"



class Story(StrEnum):
    LOGIN_VALID = "Login user with valid data"
    LOGIN_INVALID = "Login user with invalid data"

    REGISTER_VALID = "Register user with valid data"
    REGISTER_INVALID = "Register user with invalid data"

    CREATE_GRADE_VALID = "Create grade with valid data"
    CREATE_GRADE_INVALID = "Create grade with invalid data"

    GET_GRADES_VALID = "Get grade with valid data"
    GET_GRADES_INVALID = "Get grade with invalid data"

    DELETE_GRADE_VALID = "Delete grade with valid data"
    DELETE_GRADE_INVALID = "Delete grade with invalid data"

    PUT_GRADE_VALID = "Update grade (put) with valid data"
    PUT_GRADE_INVALID = "Update grade (put) with invalid data"

    GET_STAT = "Get stat"


class Label(StrEnum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
