from user import User
    
class Privilege:
    """
    A class that models the privileges list
    """

    def __init__(self):
        self.privileges = [
            "can add posts",
            "can delete post",
            "can ban user",
            "can unban user",
            "can access deleted posts"
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """
    A simple class representing a specific kind of user
    """

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = Privilege()

    def show_privileges(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f"Admin {full_name}, has the following privileges:")
        self.privileges.show_privileges()


