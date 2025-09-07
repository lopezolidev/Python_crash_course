"""
Testing errors when casting letters into numbers
"""


try:
    numerator = input("Insert numerator: ")
    denominator = input("Insert denominator: ")
    sum = int(numerator) + int(denominator)
except ValueError:
    print("Numerator or Denominator are not numbers")
else:
    print(sum)
