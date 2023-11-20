def city_country(city, country):
    """Gives cities and their countries a new format""" 
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

while True:
    print("\nPlease tell me a city and its country.")
    print("(You can quit anytime by typing 'q')")
 
    city = input("City name: ")
    if city.lower() == "q":
        break
    country = input ("Country name: ")
    if country.lower() == "q":
        break   
    
    formatted_city_country = city_country(city, country)
    print(formatted_city_country)