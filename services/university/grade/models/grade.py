from pydantic import BaseModel


class GradeRequest(BaseModel):
    teacher_id: int
    student_id: int
    grade: int

class GradeResponse(GradeRequest):
    id: int