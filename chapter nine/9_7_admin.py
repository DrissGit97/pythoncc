class User:
    """A model representing a userbase"""
    def __init__(self, first_name, last_name, joining_date, last_active_date, description):
            self.first_name = first_name
            self.last_name= last_name
            self.joining_date = joining_date
            self.last_active_date = last_active_date
            self.description = description
            self.login_attempts = 0

    def describe_user(self):
        """Broadly describes the user"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} joined on {self.joining_date} and was last active on {self.last_active_date}; Here's a brief description about them: \t{self.description} ")

    def greet_user(self):
        """Greets the user"""
        print(f"\n Welcome back, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increases login attempts by one (1)"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts"""
        self.login_attempts = 0


user_1 = User('User_fn1','User_ln1','User_jd1', 'User_lad1', 'User_des1')
print(f"Current number of login attempts: {user_1.login_attempts}")
print("Failed attempt to log in (1): ")
user_1.increment_login_attempts()
print("Failed attempt to log in (2): ")
user_1.increment_login_attempts()
print("Failed attempt to log in (3): ")
user_1.increment_login_attempts()
print("Failed attempt to log in (4): ")
user_1.increment_login_attempts()

print(f"Current number of login attempts (after update): {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Current number of login attempts (after reset): {user_1.login_attempts}")


print(f"\nNext part of the exercise: ")
print("test")

class Admin(User):
    "Represents an admin within the user system"

    def __init__(self, first_name, last_name, joining_date, last_active_date, description):
        """Initializes the atributes from the parent class"""
        super().__init__(first_name, last_name, joining_date, last_active_date, description)
        self.privileges = ["Banning users"]

    def desc_privileges(self):
        """Prints a statement about the privileges the user has"""
        print(f"This user has the following privileges: {self.privileges}")

userA = Admin('User_fnA','User_lnA','User_jdA', 'User_ladA', 'User_desA')
userA.describe_user()
userA.desc_privileges()