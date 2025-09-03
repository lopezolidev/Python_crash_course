class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is the {self.restaurant_name} restaurant and we serve "
              f"{self.cuisine_type} food")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")

    def set_number_served(self, customers):
        if customers > 0:
            self.number_served = customers
        else:
            print("You cannot ser negative number of customers")

    def incremenet_number_served(self, customers):
        if customers > 0:
            self.number_served += customers
        else:
            print("A negative number of customers cannot be served in the res" \
            "taurant")

restaurant = Restaurant('Hby', 'modern')

restaurant.number_served = 30
print(restaurant.number_served)
# 30

restaurant.set_number_served(80)
print(restaurant.number_served)
# 80

restaurant.incremenet_number_served(20)
print(restaurant.number_served)
# 100