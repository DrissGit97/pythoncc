class Employee:
    """Stores information about employees"""

    def __init__(self, fname, lname, AnSalary):
        self.fname = fname
        self.lname = lname
        self.AnSalary = AnSalary

    def give_raise(self, amount = 5000):
        """Gives the employee a raise"""
        self.AnSalary += amount