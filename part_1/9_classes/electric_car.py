class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # an attribute we don't pass
        self.litters = 10

    def get_descriptive_name(self): # to refer to an attribute, we send 'self'
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

    def fill_gas_tank(self, litters):
        self.litters += litters
        print(f"You have filled the car with {litters}, now the car has "
              f"{self.litters} gas litters")

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

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
"""
2019 Tesla Model S
"""
# my_tesla.describe_battery()

my_tesla.fill_gas_tank()
# here the method is overrun and executes a different code
"""
This car doesn't need a gas tank!
"""

my_tesla.battery.describe_battery() 
# calling the method from the instance of battery 
"""
This car has a 75-kWh battery.
"""

my_tesla.battery.get_range()
"""
This car can go about 260 miles on a full charge.
"""

my_ford = Car('ford', 'f350', 2024)
print(my_ford.get_descriptive_name())
my_ford.fill_gas_tank(5) # here we fill the gas tank bc it's not an electric car

