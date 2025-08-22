# generate a list of the first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or 
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# simple statistics
numbers = list(range(0, 10))

print(min(numbers)) # 0
print(max(numbers)) # 9
print(sum(numbers)) # 45

# now making the squares list in a 'list comprehension'

numbers = [((value ** 2) + 3) / 5 for value in range(1, 11)]
print(numbers)
# [0.8, 1.4, 2.4, 3.8, 5.6, 7.8, 10.4, 13.4, 16.8, 20.6]

letters = [vocal.title() for vocal in ['a', 'e', 'i', 'o', 'u']]
print(letters)
# ['A', 'E', 'I', 'O', 'U']

