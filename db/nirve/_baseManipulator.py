from db._general import GeneralDbManipulator
from db.nirve.bendingSkills import NirveBendingSkillsDbManipulator
from db.nirve.characterClass import NirveCharacterClassDbManipulator
from db.nirve.disadvantage import NirveDisadvantageDbManipulator
from db.nirve.item import NirveItemDbManipulator
from db.nirve.race import NirveRaceDbManipulator
from db.nirve.religion import NirveReligionDbManipulator
from db.nirve.skill import NirveSkillDbManipulator
from db.nirve.spell import NirveSpellDbManipulator

class NirveBaseDbManager():
    def __init__(self) -> None:
        self.bendingSkills = NirveBendingSkillsDbManipulator()
        self.characterClass = NirveCharacterClassDbManipulator()
        self.disadvantage = NirveDisadvantageDbManipulator()
        self.item = NirveItemDbManipulator()
        self.race = NirveRaceDbManipulator()
        self.religion = NirveReligionDbManipulator()
        self.skill = NirveSkillDbManipulator()
        self.spell = NirveSpellDbManipulator()