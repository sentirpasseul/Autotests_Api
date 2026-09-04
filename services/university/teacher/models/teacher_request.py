from pydantic import BaseModel
from services.university.group.models.subjects import Subjects


class TeacherRequest(BaseModel):
    first_name: str
    last_name: str
    subject: Subjects