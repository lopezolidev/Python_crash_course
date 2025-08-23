favorite_languages = {
    'jen' : 'python' ,
    'sarah'  : 'c' ,
    'edward' : 'ruby' ,
    'phil' : 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
'''
Hi Jen
Hi Sarah
        Sarah, I see you love C!
Hi Edward
Hi Phil
        Phil, I see you love Python!
Erin, please take our poll!
'''

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
# Sarah's favorite language is C

for name, language in favorite_languages.items():
    print(f"\n{name.title()} favourite language is {language.title()}.")
'''
Jen favourite language is Python.

Sarah favourite language is C.

Edward favourite language is Ruby.

Phil favourite language is Python.
'''



# -----------------------------------------------------------------------------

# just looping through the keys

for name in favorite_languages.keys():
    print({name.title()})
'''
{'Jen'}
{'Sarah'}
{'Edward'}
{'Phil'}
'''

# the result is not the same, the output looks different and are different DS

for name in favorite_languages:
    print(name.title())
'''
Jen
Sarah
Edward
Phil
'''

if {'Jen'} == 'Jen' :
    print("They're the same")
else:
    print("They're not")
# They're not

# -----------------------------------------------------------------------------
favorite_languages = {
    'jen' : 'python' ,
    'sarah'  : 'c' ,
    'edward' : 'ruby' ,
    'phil' : 'python'
}

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll")
'''
Edward, thank you for taking the poll
Jen, thank you for taking the poll
Phil, thank you for taking the poll
Sarah, thank you for taking the poll
'''

for language in favorite_languages.values():
    print(language.title())
'''
Python
C
Ruby
Python
'''

#-----------------------------------------------------------------------------
# now avoiding repetitive items

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'maria': 'java',
    'chris': 'c++',
    'alex': 'javascript',
    'jessica': 'python',
    'michael': 'java',
    'linda': 'c#'
}

for language in set(favorite_languages.values()):
    print(language.title())
'''
C
C#
Java
Python
Ruby
Javascript
C++

a non repetitive set of elements thanks to the 'set()' method
'''

favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python' , 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) == 1 :
        print(f"{name.title()}'s favorite language is {languages[0].title()}")        
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print("\n\t" + language)
'''
Jen's favorite languages are:

        python

        ruby
Sarah's favorite language is C

Edward's favorite languages are:

        ruby

        go

Phil's favorite languages are:

        python

        haskell
'''

