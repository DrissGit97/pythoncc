from random import randint

class Die:
    """A representation of a die"""
    def __init__ (self, sides = 6):
        """Initialize the attributes"""
        self.sides = sides

    def roll_die(self):
        "Rolls a number between 1 and 6, both included"
        print(f"You rolled a {randint(1, self.sides)}!")

print("\nYou rolled a six-sided dice: ")
six_sided_die = Die ()
six_sided_die.roll_die()

print("\nYou rolled a ten-sided dice: ")
six_sided_die = Die (10)
six_sided_die.roll_die()

print("You rolled a twenty-sided dice: ")
six_sided_die = Die (20)
six_sided_die.roll_die()