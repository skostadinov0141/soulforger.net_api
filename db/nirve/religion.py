import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveReligionDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postReligion(self,skill:NirveBaseModel) -> bool:
        return self.getCollection("nirve_religion").insert_one(skill.dict()).inserted_id
    
    def getReligions(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_religion").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getReligion(self, id: str) -> dict:
        return self.getCollection("nirve_religion").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putReligion(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_religion").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteReligion(self, id: str) -> bool:
        return self.getCollection("nirve_religion").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    