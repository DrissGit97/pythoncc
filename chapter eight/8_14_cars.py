def car_info(manufacturer, model, **etc):
    """Builds information of a car into a dictionary"""
    etc['manufacturer'] = manufacturer
    etc['model'] = model
    return etc

car_profile = car_info('Subaru', 'Outback', color="blue", tow_package=True)
print(car_profile)