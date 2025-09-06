from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# 2019 Audi A4

# my_new_car.odometer_reading = 23 ← updating the value through dot notation
# my_new_car.read_odometer()
# # This car has 23 miles on it.

my_new_car.update_odometer(23)
my_new_car.read_odometer()
# This car has 23 miles on it. ← controlling odometer value through a method

# my_new_car.update_odometer(12)
# You can't roll back an odometer!

my_new_car.increment_odometer(120)
my_new_car.read_odometer()
# This car has 143 miles on it.
