from pydantic import BaseModel


class GroupRequest(BaseModel):
    id: int = None
    name: str