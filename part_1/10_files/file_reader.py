filename = 'pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt' 
# the pwd is the folder where the terminal opens 

with open(filename) as file_object:
    # contents = file_object.read()

    lines = file_object.readlines() 
    # must be commented, if not ahead code wont execute

    for line in file_object:
        print(line.rstrip())
    """
    3.1415926535
      8979323846
      2643383279
    """
    # reading line by line

print(lines)
# ['3.1415926535\n', '  8979323846\n', '  2643383279']

for line in lines:
    print(line.rstrip())
"""
3.1415926535
  8979323846
  2643383279
"""

# print(contents.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# 3.141592653589793238462643383279...
# print(len(pi_string))
# 1_000_002

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")