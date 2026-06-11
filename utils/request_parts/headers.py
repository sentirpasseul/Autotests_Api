from enum import StrEnum


class Headers(StrEnum):
    CONTENT_TYPE_JSON = 'application/json'
    CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
