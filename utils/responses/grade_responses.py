from enum import StrEnum


class GradeResponse(StrEnum):
    GRADE_DELETED = 'Grade deleted'

class GradeErrorResponses(StrEnum):
    GRADE_NOT_FOUND = 'Grade not found'