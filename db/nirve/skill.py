import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveSkillDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postSkill(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_skill").insert_one(skill.dict()).inserted_id)
    
    def getSkills(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_skill").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getSkill(self, id: str) -> dict:
        return self.getCollection("nirve_skill").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putSkill(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_skill").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteSkill(self, id: str) -> bool:
        return self.getCollection("nirve_skill").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    