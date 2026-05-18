from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class UserResponse(User):
    id: int
    is_enabled: bool
