from pydantic import BaseModel


class StudentRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    degree: str
    phone: str
    group_id: int