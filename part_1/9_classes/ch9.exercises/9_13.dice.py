from random import randint

class Die:
    """
    A simple class that models a dice
    """

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

my_die = Die(6)
my_die.roll_die()

print("\n")

print("10-side die rolling: ...")

my_die = Die(10)
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()

print("\n")

print("20-side die rolling: ...")

my_die = Die(20)
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()


