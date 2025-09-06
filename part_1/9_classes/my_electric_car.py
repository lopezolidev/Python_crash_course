# from car import Car, ElectricCar
# import car ← a good alternate option, no naming issues
# from car import * ← not recommended 
from car import Car
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2019)

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

