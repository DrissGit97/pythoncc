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