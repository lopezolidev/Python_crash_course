venezuelan_rivers = {
    'Orinoco': 'Bolívar and Delta Amacuro states',
    'Apure': 'Apure and Guárico states',
    'Caroní': 'Bolívar state',
    'Meta': 'Apure state'
}

for river, location in venezuelan_rivers.items():
    print(f"The {river.title()} runs throug the {location}")
'''
The Orinoco runs throug the Bolívar and Delta Amacuro states
The Apure runs throug the Apure and Guárico states
The Caroní runs throug the Bolívar state
The Meta runs throug the Apure state
'''

for river in venezuelan_rivers.keys():
    print(river)
'''
Orinoco
Apure
Caroní
Meta
'''

for location in venezuelan_rivers.values():
    print(location)
'''
Bolívar and Delta Amacuro states
Apure and Guárico states
Bolívar state
Apure state
'''
