factions = {
    'unsc' : {
        'terrain vehicles' : ['warthog' , 'elephant', 'kodiak', 'mantis', 'grizzly', 'scorpion', 'mongoose'],
        'sea vehicles' : ['prowler'],
        'air vehicles' : ['pelican', 'hornet', 'falcon', 'wasp', 'sabre', 'albatross']
        },

    'covenant' : {
        'terrain vehicles' : ['ghost', 'wraith', 'chopper', 'locust', 'marauder', 'revenant', 'spectre'],
        'sea vehicles' : ['mule'],
        'air vehicles' : ['banshee', 'phantom', 'spirit', 'seraph', 'lich']
    },

    'forerunner' : {
        'terrain vehicles' : ['armiger', 'war sphinx'],
        'sea vehicles' : [],
        'air vehicles' : ['phaeton', 'harrier', 'sentinel']
    }
}


for faction in factions:
    
    print(f"The faction {faction.title()}, has available the following vehicles: ")
    
    for element, vehicles in factions[faction].items():
        print(f"{element.title()}:")
    
        if len(vehicles) == 0:
            print(f"There're no {element.title()} for the {faction.title()}")
        else:
            for vehicle in vehicles:
                print(f"\t{vehicle.title()}")       