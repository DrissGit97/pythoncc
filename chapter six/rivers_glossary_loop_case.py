rivers = {
    "nile" : "Egypt",
    "river b" : "Country B",
    "river c" : "Country C",
}

#The 'river' flows through 'Country'
for river, country in rivers.items():
    print(f"\nThe {river.lower()} runs through {country.title()}") 

#List of rivers
for country in rivers.values():
    print(f"\n{country.title()} is a country.")

#List of countries
for river in rivers.keys():
    print(f"\nThe {river.title()} is a river.")