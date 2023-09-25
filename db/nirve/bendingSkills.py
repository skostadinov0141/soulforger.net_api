import json

from bson import ObjectId
from db._general import GeneralDbManipulator
from models.nirve.baseModel import NirveBaseModel

class NirveBendingSkillsDbManipulator(GeneralDbManipulator):

    def __init__(self) -> None:
        super().__init__()

    def postBendingSkill(self,skill:NirveBaseModel) -> bool:
        return str(self.getCollection("nirve_bending_skills").insert_one(skill.dict()).inserted_id)
    
    def getBendingSkills(self, query: str) -> list[dict]:
        return list(self.getCollection("nirve_bending_skills").find(
            json.loads(query),
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        ))
    
    def getBendingSkill(self, id: str) -> dict:
        return self.getCollection("nirve_bending_skills").find_one(
            {"_id": ObjectId(id)},
            {
                "_id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
            }
        )
    
    def putBendingSkill(self, id: str, skill: NirveBaseModel) -> bool:
        return self.getCollection("nirve_bending_skills").update_one(
            {"_id": ObjectId(id)},
            {"$set": skill.dict(exclude_unset=True)}
        ).modified_count == 1
    
    def deleteBendingSkill(self, id: str) -> bool:
        return self.getCollection("nirve_bending_skills").delete_one(
            {"_id": ObjectId(id)}
        ).deleted_count == 1
    