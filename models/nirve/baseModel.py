from pydantic import BaseModel

class NirveBaseModel(BaseModel):
    _id: str | None
    name: str
    description: str