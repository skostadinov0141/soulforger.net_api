import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveCharacterClassDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postCharacterClass(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_character_class").insert_one(skill.dict()).inserted_id)
    
    def getCharacterClasses(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_character_class").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getCharacterClass(self, id: str) -> dict:
        return self.getCollection("nirve_character_class").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putCharacterClass(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_character_class").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteCharacterClass(self, id: str) -> bool:
        return self.getCollection("nirve_character_class").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    