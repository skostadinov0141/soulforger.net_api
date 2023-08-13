from db.account_management import AccountDbManipulator


class DbManager():

    def __init__(self) -> None:
        self.accounts = AccountDbManipulator()
    