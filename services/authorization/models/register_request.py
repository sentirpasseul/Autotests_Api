from pydantic import BaseModel


class RegisterRequest(BaseModel):
    username: str
    password: str
    password_repeat: str
    email: str