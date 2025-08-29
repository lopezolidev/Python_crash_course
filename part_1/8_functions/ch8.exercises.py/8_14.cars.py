def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    return car_info

car = make_car('ford', 'f250', color='black', tow_package=True)

print(car)
# {'color': 'black', 
# 'tow_package': True, 
# 'manufacturer': 'ford', 
# 'model': 'f250'}