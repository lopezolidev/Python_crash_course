favorite_places = {
    'jacqueline' : ['porky mountain', 'west desert', 'small town beach'],
    'mariangel' : ['city mountain', 'cow county', 'south jungle'],
    'eli' : ['old town', 'camping fields', 'east side campus']
}

for person, places in favorite_places.items():
    print(f"\n{person.title()} likes to go to:")
    for place in places:
        print(f"\t" + place.title())
'''
Jacqueline likes to go to:
        Porky Mountain
        West Desert
        Small Town Beach

Mariangel likes to go to:
        City Mountain
        Cow County
        South Jungle

Eli likes to go to:
        Old Town
        Camping Fields
        East Side Campus
'''

