from pydantic import BaseModel, Field
from enum import Enum


class Grade(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class GradeRequest(BaseModel):
    teacher_id: int = Field(...)
    student_id: int = Field(...)
    grade: int = Field(...)


class GradeResponse(GradeRequest):
    id: int = Field(...)

class GradeStatRequest(BaseModel):
    student_id: int
    teacher_id: int
    group_id: int

class GradeStatResponse(BaseModel):
    count: int | None = Field(...)
    min: int | None = Field(...)
    max: int | None = Field(...)
    avg: float | None = Field(...)


