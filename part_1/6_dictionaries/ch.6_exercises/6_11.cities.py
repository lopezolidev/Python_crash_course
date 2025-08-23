cities = {
    'Cairo' :{
        'country' : 'egypt',
        'population' : 'approx. 9.8 million',
        'fact' :'Cairo is home to the Giza pyramid complex and the ancient city of Memphis.'
    },
    'Istambul' :{
        'country' : 'Turkey',
        'population' : 'Istanbul is a transcontinental city, bridging Europe and Asia across the Bosphorus Strait.' ,
        'fact' :''
    },

    'Mina Gerais' :{
        'country' : 'Brazil',
        'population' : 'approx. 21.4 million',
        'fact' : 'Minas Gerais is known for its colonial-era towns, particularly Ouro Preto and Diamantina.'
    }
}

for city, city_info in cities.items():
    print(f"\nWelcome to {city.title()}! These are the following facts:")
    for info, data in city_info.items():
        print(f"{info.title()}:")
        print(f"\t{data}")
'''

Welcome to Cairo! These are the following facts:
Country:
        egypt
Population:
        approx. 9.8 million
Fact:
        Cairo is home to the Giza pyramid complex and the ancient city of Memphis.

Welcome to Istambul! These are the following facts:
Country:
        Turkey
Population:
        Istanbul is a transcontinental city, bridging Europe and Asia across the Bosphorus Strait.
Fact:


Welcome to Mina Gerais! These are the following facts:
Country:
        Brazil
Population:
        approx. 21.4 million
Fact:
        Minas Gerais is known for its colonial-era towns, particularly Ouro Preto and Diamantina.
'''