from email import message
from pydantic import BaseModel

class RequestBody(BaseModel):
    message: str
