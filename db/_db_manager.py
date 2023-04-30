from db.account_management import AccountDbManipulator
from db.general import GeneralDbManipulator
from db.profiles import ProfilesDbManipulator


class DbManager():

    def __init__(self) -> None:
        self.general = GeneralDbManipulator()
        self.accounts = AccountDbManipulator()
        self.profiles = ProfilesDbManipulator()
    
    