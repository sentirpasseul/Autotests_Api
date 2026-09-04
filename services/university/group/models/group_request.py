from pydantic import BaseModel


class GroupRequest(BaseModel):
    name: str