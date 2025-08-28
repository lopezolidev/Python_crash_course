def high_and_low(numbers):
    numbers = numbers.split(' ')
    max = int(numbers[0])
    min = int(numbers[0])

    for number in numbers:
        if max < int(number):
            max = int(number)
        elif min > int(number):
            min = int(number)
    
    return f"{str(max)} {str(min)}"

# must return the highest and the lowest numbers in a string of numbers