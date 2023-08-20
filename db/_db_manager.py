from db.auth import AccountDbManipulator
from db.user import UserDbManipulator


class DbManager():

    def __init__(self) -> None:
        self.auth = AccountDbManipulator()
        self.user = UserDbManipulator()
    