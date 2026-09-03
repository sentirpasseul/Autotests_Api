from pydantic import BaseModel, Field
from enum import Enum


class GradeRequest(BaseModel):
    teacher_id: int
    student_id: int
    grade: int  


class GradeCreateResponse(GradeRequest):
    id: int  

class GradeStatRequest(BaseModel):
    student_id: int
    teacher_id: int
    group_id: int

class GradeStatResponse(BaseModel):
    count: int | None  
    min: int | None  
    max: int | None  
    avg: float | None  

class GradeUpdateResponse(BaseModel):
    teacher_id: int  
    student_id: int  
    grade: int  
    id: int  



