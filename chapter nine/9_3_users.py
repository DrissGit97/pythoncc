class User:
    """A model representing a userbase"""
    def __init__(self, first_name, last_name, joining_date, last_active_date, description):
            self.first_name = first_name
            self.last_name= last_name
            self.joining_date = joining_date
            self.last_active_date = last_active_date
            self.description = description

    def describe_user(self):
        """Broadly describes the user"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} joined on {self.joining_date} and was last active on {self.last_active_date}; Here's a brief description about them: \t{self.description} ")

    def greet_user(self):
        """Greets the user"""
        print(f"\n Welcome back, {self.first_name.title()}!")


user_1 = User('User_fn1','User_ln1','User_jd1', 'User_lad1', 'User_des1')
print("\nCalling 'describe_user': ")
user_1.describe_user()
print("\nCalling 'greet_user': ")
user_1.greet_user()

user_2 = User('User_fn2','User_ln2','User_jd2', 'User_lad2', 'User_des2')
print("\nCalling 'describe_user': ")
user_2.describe_user()
print("\nCalling 'greet_user': ")
user_2.greet_user()

user_3 = User('User_fn3','User_ln3','User_jd3', 'User_lad3', 'User_des3')
print("\nCalling 'describe_user': ")
user_3.describe_user()
print("\nCalling 'greet_user': ")
user_3.greet_user()