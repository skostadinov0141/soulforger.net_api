from db.account_management import AccountDbManipulator
from db.contributions import ContributionsDbManipulator
from db.general import GeneralDbManipulator
from db.profiles import ProfilesDbManipulator
from db.wiki import WikiDbManipulator


class DbManager():

    def __init__(self) -> None:
        self.general = GeneralDbManipulator()
        self.accounts = AccountDbManipulator()
        self.profiles = ProfilesDbManipulator()
        self.wiki = WikiDbManipulator()
        self.contributions = ContributionsDbManipulator()
    
    