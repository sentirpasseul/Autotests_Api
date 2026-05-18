from enum import StrEnum

from pydantic import BaseModel


class Student(BaseModel):
    student_id: int

class DegreeEnum(StrEnum):
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"