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

user_1 = User('Joe', 'Doe')

print(user_1.login_attempts) # 0

user_1.increment_login_attempts()
print(user_1.login_attempts) # 1

user_1.increment_login_attempts()
print(user_1.login_attempts) # 2
 
user_1.increment_login_attempts()
print(user_1.login_attempts) # 3

user_1.increment_login_attempts()
print(user_1.login_attempts) # 4

user_1.reset_login_attempts()
print(user_1.login_attempts) # 0
