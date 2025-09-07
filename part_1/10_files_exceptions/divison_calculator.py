numerator = input("insert numerator:  ")
denominator = input("insert denominator:  ")

try:
    division = int(numerator) / int(denominator)
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(division)