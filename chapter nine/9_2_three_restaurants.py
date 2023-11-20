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


restaurant_1 = Restaurant ('Name_1', 'Cuisine_type_1')
print("\nThe following is printed through the 'describe' command (for restaurant_1):")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant ('Name_2', 'Cuisine_type_2')
print("\nThe following is printed through the 'describe' command (for restaurant_2):")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant ('Name_3', 'Cuisine_type_3')
print("\nThe following is printed through the 'describe' command (for restaurant_3):")
restaurant_3.describe_restaurant()