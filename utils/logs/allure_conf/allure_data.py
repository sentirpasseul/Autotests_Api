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
    GRADES = "Grades Managements"
    GROUPS = "Groups Managements"
    STUDENTS = "Students Managements"
    TEACHERS = "Teachers Managements"


class Feature(StrEnum):
    AUTH = "Authorization"
    REGISTER = "Registration"

    CREATE_GRADE = "Create grade"
    GET_GRADES = "Get grade"
    DELETE_GRADE = "Delete grade"

    UPGRADE_GRADE_PUT = "Upgrade grade (put)"

    GET_STAT = "Get statistics"

    CREATE_GROUP = "Create group"
    DELETE_GROUP = "Delete group"
    GET_GROUP = "Get group"
    GET_GROUPS = "Get groups"
    UPDATE_GROUP_PUT = "Upgrade (put) group by group_id"

    CREATE_STUDENT = "Create student"
    DELETE_STUDENT = "Delete student"
    GET_STUDENT = "Get student"
    GET_STUDENTS = "Get students"
    UPDATE_PUT_STUDENT = "Update (put) student by student_id"

    CREATE_TEACHER = "Create teacher"
    DELETE_TEACHER = "Delete teacher"
    GET_TEACHER = "Get teacher"
    GET_TEACHERS = "Get teachers"
    UPDATE_PUT_TEACHER = "Update (put) teacher by teacher_id"


class Story(StrEnum):
    CREATE_VALID = "Create with valid data"
    CREATE_INVALID = "Create with invalid data"

    GET_VALID = "Get valid data"
    GET_INVALID = "Get invalid data"

    UPDATE_PUT_VALID = "Update (put) valid data"
    UPDATE_PUT_INVALID = "Update (put) invalid data"

    DELETE_VALID = "Delete with valid data"
    DELETE_INVALID = "Delete with invalid data"

    LOGIN_VALID = "Login user with valid data"
    LOGIN_INVALID = "Login user with invalid data"

    REGISTER_VALID = "Register user with valid data"
    REGISTER_INVALID = "Register user with invalid data"


class Label(StrEnum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
