from pydantic import BaseModel
from utilities.characterSchemeGenerator import generateTalentList, generateCombatSkillList

class PrimaryAttributes(BaseModel):
    MU:int = 0
    KL:int = 0
    IN:int = 0
    CH:int = 0
    FF:int = 0
    GE:int = 0
    KO:int = 0
    KK:int = 0

class CappedInt(BaseModel):
    current:int = 0
    max:int = 0

class SecondaryAttributes(BaseModel):
    LEP:CappedInt = CappedInt().dict()
    ASP:CappedInt = CappedInt().dict()
    KAP:CappedInt = CappedInt().dict()
    SK:CappedInt = CappedInt().dict()
    ZK:CappedInt = CappedInt().dict()
    AW:CappedInt = CappedInt().dict()
    INI:CappedInt = CappedInt().dict()
    GES:CappedInt = CappedInt().dict()
    WS:CappedInt = CappedInt().dict()

class Talent(BaseModel):
    name:str = ""
    category:str = ""
    att_1:str = ""
    att_2:str = ""
    att_3:str = ""
    fw:int = 0

class CombatSkill(BaseModel):
    name:str = ""
    lf:str = ""
    at:int = 0
    pa:int = 0

class CloseRangeWeapon(BaseModel):
    name:str = ""
    combat_skill:str = ""
    damage_die_count:int = 0
    damage_die:int = 0
    damage_mod:int = 0
    range:str = ""
    at:int = 0
    pa:int = 0

class LongRangeWeapon(BaseModel):
    name:str = ""
    combat_skill:str = ""
    damage_die_count:int = 0
    damage_die:int = 0
    damage_mod:int = 0
    range:str = ""
    at:int = 0

class Armor(BaseModel):
    name:str = ""
    sw:int = 0
    rs:int = 0
    gs_ini_mod:int = 0

class StatusEffect(BaseModel):
    name:str = ""
    level:CappedInt

class Funds(BaseModel):
    d:int = 0
    s:int = 0
    h:int = 0
    k:int = 0

class DSACharacter(BaseModel):
    # Base Attributes
    name:str = ""
    level:str = ""
    family:str = ""
    birth_date:str = ""
    species:str = ""
    culture:str = ""
    profession:str = ""
    age:int = 0
    sex:str = ""
    height:int = 0

    # Primary Attributes
    primary_attributes:PrimaryAttributes = PrimaryAttributes().dict()

    # Secondary Attributes
    secondary_attributes:SecondaryAttributes = SecondaryAttributes().dict()

    # Talents -> reference the Talent model
    talents:list = generateTalentList()

    # Combat Skills -> reference the CombatSkill model
    combat_skills:list = generateCombatSkillList()

    # Close Range weapons -> reference the CloseRangeWeapon model
    close_range_weapons:dict = {}

    # Long Range weapons -> reference the LongRangeWeapon model
    long_range_weapons:dict = {}

    # Armor -> reference the Armor model
    armor:dict = {}

    # Status Effects -> reference the StatusEffect model
    status_effects:dict = {}

    # Funds
    funds:Funds = Funds().dict()



