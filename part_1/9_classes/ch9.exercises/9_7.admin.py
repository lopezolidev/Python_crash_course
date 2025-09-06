class User:
    """A simple class representing an user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: {self.first_name}\nUser lastname: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
class Admin(User):
    """
    A simple class representing a specific kind of user
    """

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = [
            "can add posts",
            "can delete post",
            "can ban user",
            "can unban user",
            "can access deleted posts"
        ]

    def show_privileges(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Admin {full_name}, has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_1 = Admin("Xavier", "Lopez")

admin_1.show_privileges()