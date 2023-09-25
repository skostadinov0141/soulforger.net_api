import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveItemDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postItem(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_item").insert_one(skill.dict()).inserted_id)
    
    def getItems(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_item").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getItem(self, id: str) -> dict:
        return self.getCollection("nirve_item").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putItem(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_item").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteItem(self, id: str) -> bool:
        return self.getCollection("nirve_item").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    