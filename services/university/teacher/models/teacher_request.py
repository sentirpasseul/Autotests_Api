from pydantic import BaseModel


class TeacherRequest(BaseModel):
    first_name: str
    last_name: str
    subject: str