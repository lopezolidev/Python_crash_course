class User:
    """A simple class representing an user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User name: {self.first_name}\nUser lastname: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")


user_1 = User('Mary', 'Doe')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Jacqueline', 'P')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Robert', 'Cip')
user_3.describe_user()
# User name: Robert
# User lastname: Cip

user_3.greet_user()
# Hello Robert!