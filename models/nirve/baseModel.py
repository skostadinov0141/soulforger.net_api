from pydantic import BaseModel

class NirveBaseModel(BaseModel):
    name: str
    description: str