from pydantic import BaseModel

class WikiSearchQuery(BaseModel):
    tags: list