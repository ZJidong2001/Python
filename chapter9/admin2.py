from admin1 import Privileges, User

class Admin(User):
    def __init__(self, first, last, loc, privileges):
        super().__init__(first, last, loc)
        self.privileges = Privileges(privileges)