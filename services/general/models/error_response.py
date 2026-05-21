from pydantic import BaseModel
from typing import List, Union


class ErrorResponse(BaseModel):
    detail: str

class ValidationErrorDetail(BaseModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class ValidationError(BaseModel):
    detail: List[ValidationErrorDetail]