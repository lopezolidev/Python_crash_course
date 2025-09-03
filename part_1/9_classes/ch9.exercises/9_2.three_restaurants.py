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

restaurant_1 = Restaurant('Tuscan', 'italian')
restaurant_1.describe_restaurant()
# This is the Tuscan restaurant and we serve italian food
restaurant_1.open_restaurant()
# The Tuscan restaurant is open!

restaurant_2 = Restaurant('Hako', 'japanese')
restaurant_2.describe_restaurant()
# This is the Hako restaurant and we serve japanese food
restaurant_2.open_restaurant()
# The Hako restaurant is open!

restaurant_3 = Restaurant('Jeffies', 'BBQ')
restaurant_3.describe_restaurant()
# This is the Jeffies restaurant and we serve BBQ food
restaurant_3.open_restaurant()
# The Jeffies restaurant is open!