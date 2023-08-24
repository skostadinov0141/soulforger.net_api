from db.auth import AccountDbManipulator
from db.profile import ProfileDbManipulator
from db.privileges import PrivilegesDbManipulator


class DbManager():

    def __init__(self) -> None:
        self.auth = AccountDbManipulator()
        self.profile = ProfileDbManipulator()
        self.privileges = PrivilegesDbManipulator()
    