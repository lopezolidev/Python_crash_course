def city_country(city, country):
    return f"{city.title()}, {country.title()}"

while True:
    print("\nPlease enter the name of a city and a country.")
    print("(Enter 'q' to end the program)")

    city = input("\nCity name: ")

    if city == 'q':
        break

    country = input("Country name: ")

    print(city_country(city, country))