from pydantic import BaseModel


class CallInfo(BaseModel):
    from_number: str
    to_number: str
