class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"This restaurant's called {self.name.title()} and specializes in {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Prints that the message is open."""
        print("The restaurant is now open")

restaurant = Restaurant ('Name_1', 'Cuisine_type_1')
print("\nThe following is printed through the 'print' command:")
print(f"{restaurant.name}")
print(f"{restaurant.cuisine_type}")

print("\nThe following is printed through the 'describe' command:")
restaurant.describe_restaurant()

print("\nThe next is printed through the 'open_restaurant' method")
restaurant.open_restaurant()