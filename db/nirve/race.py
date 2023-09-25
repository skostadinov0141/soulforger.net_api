import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveRaceDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postRace(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_race").insert_one(skill.dict()).inserted_id)
    
    def getRaces(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_race").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getRace(self, id: str) -> dict:
        return self.getCollection("nirve_race").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putRace(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_race").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteRace(self, id: str) -> bool:
        return self.getCollection("nirve_race").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1