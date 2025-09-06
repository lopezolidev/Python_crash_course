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

class IceCreamStand(Restaurant):

    """A class that models an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        A method that initializes the attributes of the child class
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'berries']

    def describe_flavors(self):
        print(f"{self.restaurant_name}'s Ice Cream Stand offers the following flavors:\n")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_iceCreamStand = IceCreamStand(restaurant_name='Cream', cuisine_type='Desserts')
my_iceCreamStand.describe_flavors()