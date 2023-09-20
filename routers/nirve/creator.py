from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile
from db._db_manager import DbManager
from models.auth.account import PrivEscalationRequest
from models.nirve.baseModel import NirveBaseModel
from routers.auth import validate_priv_level, validate_token
from datetime import datetime
from cloudinary.uploader import upload, destroy
from typing import Annotated


db = DbManager()


# region Router
router = APIRouter(
    prefix='/nirve/creator',
    tags=['Nirve Creator']
)
# endregion



# region API Methods

@router.get('/bending-skills', description='Returns a list of bending skills based on the given query')
def get_bending_skills(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.bendingSkills.paginate(db.nirve.bendingSkills.getBendingSkills(query), page, page_size)) 
    return list(db.nirve.bendingSkills.getBendingSkills(query))

@router.get('/bending-skills/{id}', description='Returns a bending skill with the given id')
def get_bending_skill(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.bendingSkills.getBendingSkill(id)

@router.post('/bending-skills', description='Creates a new bending skill')
def create_bending_skill(bending_skill:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.bendingSkills.postBendingSkill(bending_skill)

@router.put('/bending-skills/{id}', description='Updates a bending skill with the given id')
def update_bending_skill(id:str, bending_skill:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.bendingSkills.putBendingSkill(id, bending_skill)

@router.delete('/bending-skills/{id}', description='Deletes a bending skill with the given id')
def delete_bending_skill(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.bendingSkills.deleteBendingSkill(id)





@router.get('/items', description='Returns a list of items based on the given query')
def get_items(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.item.paginate(db.nirve.item.getItem(query), page, page_size)) 
    return list(db.nirve.item.getItems(query))

@router.get('/items/{id}', description='Returns a item with the given id')
def get_item(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.item.getItem(id)

@router.post('/items', description='Creates a new item')
def create_item(item:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.item.postItem(item)

@router.put('/items/{id}', description='Updates a item with the given id')
def update_item(id:str, item:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.item.putItem(id, item)

@router.delete('/items/{id}', description='Deletes a item with the given id')
def delete_item(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.item.deleteItem(id)





@router.get('/spells', description='Returns a list of spells based on the given query')
def get_spells(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.spell.paginate(db.nirve.spell.getSpells(query), page, page_size)) 
    return list(db.nirve.spell.getSpells(query))

@router.get('/spells/{id}', description='Returns a spell with the given id')
def get_spell(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.spell.getSpell(id)

@router.post('/spells', description='Creates a new spell')
def create_spell(spell:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.spell.postSpell(spell)

@router.put('/spells/{id}', description='Updates a spell with the given id')
def update_spell(id:str, spell:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.spell.putSpell(id, spell)

@router.delete('/spells/{id}', description='Deletes a spell with the given id')
def delete_spell(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.spell.deleteSpell(id)





@router.get('/character-classes', description='Returns a list of character classes based on the given query')
def get_character_classes(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.characterClass.paginate(db.nirve.characterClass.getCharacterClasses(query), page, page_size)) 
    return list(db.nirve.characterClass.getCharacterClasses(query))

@router.get('/character-classes/{id}', description='Returns a character class with the given id')
def get_character_class(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.characterClass.getCharacterClass(id)

@router.post('/character-classes', description='Creates a new character class')
def create_character_class(character_class:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.characterClass.postCharacterClass(character_class)

@router.put('/character-classes/{id}', description='Updates a character class with the given id')
def update_character_class(id:str, character_class:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.characterClass.putCharacterClass(id, character_class)

@router.delete('/character-classes/{id}', description='Deletes a character class with the given id')
def delete_character_class(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.characterClass.deleteCharacterClass(id)





@router.get('/disadvantages', description='Returns a list of disadvantages based on the given query')
def get_disadvantages(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.disadvantage.paginate(db.nirve.disadvantage.getDisadvantages(query), page, page_size)) 
    return list(db.nirve.disadvantage.getDisadvantages(query))

@router.get('/disadvantages/{id}', description='Returns a disadvantage with the given id')
def get_disadvantage(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.disadvantage.getDisadvantage(id)

@router.post('/disadvantages', description='Creates a new disadvantage')
def create_disadvantage(disadvantage:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.disadvantage.postDisadvantage(disadvantage)

@router.put('/disadvantages/{id}', description='Updates a disadvantage with the given id')
def update_disadvantage(id:str, disadvantage:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.disadvantage.putDisadvantage(id, disadvantage)

@router.delete('/disadvantages/{id}', description='Deletes a disadvantage with the given id')
def delete_disadvantage(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.disadvantage.deleteDisadvantage(id)





@router.get('/races', description='Returns a list of races based on the given query')
def get_races(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.race.paginate(db.nirve.race.getRaces(query), page, page_size)) 
    return list(db.nirve.race.getRaces(query))

@router.get('/races/{id}', description='Returns a race with the given id')
def get_race(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.race.getRace(id)

@router.post('/races', description='Creates a new race')
def create_race(race:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.race.postRace(race)

@router.put('/races/{id}', description='Updates a race with the given id')
def update_race(id:str, race:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.race.putRace(id, race)

@router.delete('/races/{id}', description='Deletes a race with the given id')
def delete_race(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.race.deleteRace(id)





@router.get('/religions', description='Returns a list of religions based on the given query')
def get_religions(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.religion.paginate(db.nirve.religion.getReligions(query), page, page_size)) 
    return list(db.nirve.religion.getReligions(query))

@router.get('/religions/{id}', description='Returns a religion with the given id')
def get_religion(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.religion.getReligion(id)

@router.post('/religions', description='Creates a new religion')
def create_religion(religion:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.religion.postReligion(religion)

@router.put('/religions/{id}', description='Updates a religion with the given id')
def update_religion(id:str, religion:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.religion.putReligion(id, religion)

@router.delete('/religions/{id}', description='Deletes a religion with the given id')
def delete_religion(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.religion.deleteReligion(id)





@router.get('/skills', description='Returns a list of skills based on the given query')
def get_skill(query:str = None, page:int|None = None, page_size:int|None = None,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    if page and page_size:
        return list(db.nirve.skill.paginate(db.nirve.skill.getSkills(query), page, page_size)) 
    return list(db.nirve.skill.getSkills(query))

@router.get('/skills/{id}', description='Returns a skill with the given id')
def get_skill(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.skill.getSkill(id)

@router.post('/skills', description='Creates a new skill')
def create_skill(skill:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.skill.postSkill(skill)

@router.put('/skills/{id}', description='Updates a skill with the given id')
def update_skill(id:str, skill:NirveBaseModel,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.skill.putSkill(id, skill)

@router.delete('/skills/{id}', description='Deletes a skill with the given id')
def delete_skill(id:str,token:dict = Depends(validate_token)):
    validate_priv_level(token, 50)
    return db.nirve.skill.deleteSkill(id)

# endregion