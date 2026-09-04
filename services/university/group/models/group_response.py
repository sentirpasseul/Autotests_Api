from pydantic import BaseModel


class GroupResponse(BaseModel):
    name: str
    id: int