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

class IceCreamStand(Restaurant):
    """Represents an ice cream stand as a subtype of restaurant"""
    def __init__(self, name, cuisine_type):
        """Initialize some attributes of the parent class """
        super().__init__(name, cuisine_type)
        self.flavors = ["A", "B", "C"]

    def av_flavors(self):
        """Prints the list of available flavors"""
        print(f"We have {self.flavors} available!")

icecreamrestaurant = IceCreamStand ('Name', 'cuisine_type')
icecreamrestaurant.av_flavors()