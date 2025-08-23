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

friends = [ 
    'sarah', 
    'Alba', 
    'Mariangel',
    'alex', 
    'jessica', 
    'linda',  
    'Oliver',
    'edward', 
    'Charles' 
]

for name in friends:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()}, for responding the poll!")
    else:
        print(f"{name.title()}, I invite you to take the poll")
'''
Thank you Sarah, for responding the poll!
Alba, I invite you to take the poll
Mariangel, I invite you to take the poll
Thank you Alex, for responding the poll!
Thank you Jessica, for responding the poll!
Thank you Linda, for responding the poll!
Oliver, I invite you to take the poll
Thank you Edward, for responding the poll!
Charles, I invite you to take the poll
'''

