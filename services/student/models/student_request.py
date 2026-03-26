from pydantic import BaseModel


class StudentsRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    degree: str
    phone: str
    group_id: int