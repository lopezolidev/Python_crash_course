"""A module containing a single Restaurant class"""
class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is the {self.restaurant_name} restaurant and we serve "
              f"{self.cuisine_type} food")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")



