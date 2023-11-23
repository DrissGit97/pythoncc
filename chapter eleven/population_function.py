def get_formatted_name(city, country, population = 'undefined'):
    """Generates a neatly formatted sentence using city and country"""
    output_string = (f"{city}, {country}")
    if population:
        output_string += f" has a population of {population}"
    return city_country.title()

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("\nPlease give me the city's country: ")
    if country == 'q':
        break
    formatted_name = get_formatted_name(city, country)
    print(f"\t Neatly formatted name: {formatted_name}")