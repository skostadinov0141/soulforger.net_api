import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveDisadvantageDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postDisadvantage(self,skill:NirveBaseModel) -> bool:
        return self.getCollection("nirve_disadvantage").insert_one(skill.dict()).inserted_id
    
    def getDisadvantages(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_disadvantage").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getDisadvantage(self, id: str) -> dict:
        return self.getCollection("nirve_disadvantage").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putDisadvantage(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_disadvantage").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteDisadvantage(self, id: str) -> bool:
        return self.getCollection("nirve_disadvantage").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    