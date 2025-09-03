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

le_moromi = Restaurant('Tuscan', 'italian')
le_moromi.describe_restaurant()
# This is the Tuscan restaurant and we serve italian food
le_moromi.open_restaurant()
# The Tuscan restaurant is open!

