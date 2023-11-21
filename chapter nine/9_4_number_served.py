class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type"""
        print(f"This restaurant's called {self.name.title()} and specializes in {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Prints that the message is open"""
        print("The restaurant is now open")
    
    def number_customers(self):
        """Prints the number of customers"""
        print(f"This restaurant has served {self.number_served} customers today.")

    def set_number_served(self, customers):
        """Defines the number of customers served today"""
        self.number_served = customers

    def increment_number_served(self, customers):
        """Adds more customers to the number of customers served today"""
        self.number_served += customers


restaurant = Restaurant ('Name_1', 'Cuisine_type_1')
print("\nThe following is printed through the 'number_customers' command:")
restaurant.number_customers()

print("\nThe following is printed after using the 'set_number_served' command:")
restaurant.set_number_served(12)
restaurant.number_customers()
#print("\nThe following is printed through the 'print' command:")
#print(f"{self.number_served}")
print("\nThe following is printed after using the 'increment_number_served' command:")
restaurant.increment_number_served(3)
restaurant.number_customers()