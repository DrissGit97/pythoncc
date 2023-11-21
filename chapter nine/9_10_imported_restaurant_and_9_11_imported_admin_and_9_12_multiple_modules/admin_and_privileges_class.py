"""Class that can be used to represent privileges and admin-related commands."""

from user_class import User
class A_privileges:
    """Represents an admin's default privileges"""

    def __init__(self, privileges=["Privilege A", "Privilege B", "Privilege C", "Privilege D"]):
        """Initializes the atributes from the parent class"""
        self.privileges = privileges

    def desc_privileges(self):
        """Prints a statement about the privileges the user has"""
        print(f"This user has the following privileges: {self.privileges}")

class Admin(User):
    """Represents an admin within the user system"""
    def __init__(self, first_name, last_name, joining_date, last_active_date, description):
        """Initializes the default attributes"""
        super().__init__(first_name, last_name, joining_date, last_active_date, description)
        self.privileges = A_privileges()

userA = Admin('User_fnA','User_lnA','User_jdA', 'User_ladA', 'User_desA')
userA.describe_user()
userA.privileges.desc_privileges()