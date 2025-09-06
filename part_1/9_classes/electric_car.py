"""A set of classes that can be used to repreent electric cars."""

from car import Car

# Battery class to abstract the battery for the electric car
class Battery:
    """Represents aspects of the battery of an electric vehicle"""

    def __init__(self, battery_size = 75):
        """Initialize battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car): # passing class 'Car' as argument
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electic car.
        """
        super().__init__(make, model, year) # calling 'super()' method inside
        self.battery = Battery()

    # def describe_battery(self):
    #     """
    #     Print a statement describing the battery size.
    #     """
    #     print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self): # overriding fill_gas_tank method
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")