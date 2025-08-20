name = "ada lovelace"

print(name.title())
# title case each word of the string is called 
# Ada Lovelace

print(name.upper())
# ADA LOVELACE

print(name.lower())
# ada lovelace

# using variables inside strings
first_name = "ada"
last_name = "lovelace"
message = f"hello, {first_name.title()} {last_name.title()}"
print(message)

# using python3.5 syntax
message = "Hello, {} {}".format(first_name, last_name)
print(message)

# printing spaces and tabs
print("Languages: \n\tPython \n\tC \n\tJava")
# printing spaces and tabs
print("Languages: \tPython \tC \tJava")
# printing spaces and tabs
print("Languages: \nPython \nC \nJava")

favourite_language = " python "
favourite_language.rstrip()
# ' python'

favourite_language.lstrip()
# 'python '

favourite_language.strip()
# 'python'

favourite_language = favourite_language.strip()

favourite_language 
# 'python'

