from db.auth import AccountDbManipulator
from db.profile import ProfileDbManipulator
from db.privileges import PrivilegesDbManipulator
from db.nirve._baseManipulator import NirveBaseDbManager


class DbManager():

    def __init__(self) -> None:
        self.auth = AccountDbManipulator()
        self.profile = ProfileDbManipulator()
        self.privileges = PrivilegesDbManipulator()
        self.nirve = NirveBaseDbManager()
    