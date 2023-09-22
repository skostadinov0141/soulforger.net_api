from pydantic import BaseModel

class NirveBaseModel(BaseModel):
    name: str
    description: str
    # . = current field in the model
    # > = the id of a list item
    location: str