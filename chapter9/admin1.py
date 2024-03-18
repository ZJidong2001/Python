class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class User:

    def __init__(self, first, last, loc):
        self.first_name = first.title()
        self.last_name = last.title()
        self.location = loc
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")

    def greeter_user(self):
        print(f'Welcome {self.first_name} {self.last_name} from {self.location}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0