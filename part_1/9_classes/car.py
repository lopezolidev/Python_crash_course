"""A class that can be used to represent a car"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # an attribute we don't pass
        self.gas_tank = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""

        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You cannot increment a negative milage!")

    def fill_gas_tank(self, litters): # overriding fill_gas_tank method
        """Method to increase gas tank of the gas car."""
        self.gas_tank += litters
        print(f"Now the {self.get_descriptive_name()} has {self.gas_tank} litters"\
              " of gas")
