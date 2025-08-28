def binary_array_to_number(arr):
    pwr = 0
    
    sum = 0
    
    for item in reversed(arr):
        if item:
            sum += 2 ** pwr
        pwr += 1
    
    return sum

print(binary_array_to_number([0,1,1,0]))