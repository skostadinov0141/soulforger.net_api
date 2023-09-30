import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveSpellDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postSpell(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_spell").insert_one(skill.dict()).inserted_id)
    
    def getSpells(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_spell").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getSpell(self, id: str) -> dict:
        return self.getCollection("nirve_spell").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putSpell(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_spell").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteSpell(self, id: str) -> bool:
        return self.getCollection("nirve_spell").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    