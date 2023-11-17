car = "honda"
print("Is car == 'honda'? I predict True.")
print(car == 'honda')

car_years=1
print("Is car age >= 0? I predict True")
print(car_years>=0)
print("Is car age <= 1? I predict True")
print(car_years<=0)

print("Is car == audi? I predict False")
print(car == 'audi')

car_keys="At home"
print("Are car keys at home? I predict True")
print(car_keys=="At home")

car_keys="At home"
print("Are car keys here? I predict False")
print(car_keys=="At home")

studying="from home" 
print("Am I studying from home? I predict true")
print(studying=="from home")

location= "home"
print("Am I in a submarine? I predict False")
print (location == "submarine")

location= "home"
print("Am I in a plane? I predict False")
print (location == "plane")

species= "human"
print("Am I a dog? I predict False")
print (species == "dog")

car= "audi"
print("Is the car an Audi? I predict True")
print(car=="Audi".lower())

car= "Nissan" 
country= "Japan"
print("Is the car a nissan and from Japan? I predict True") 
print(car=="nissan".title() and country=="Japan".title())

car= "German_brand" 
country= "Japan"
print("Is the car a german_brand or from Japan? I predict True") 
print(car=="German_brand".title() or country=="Japan".title())

years=("2001","2002","2003")
print("Is 2001 included in the list?")
print("2001" in years)

year="2004"
if year not in years:
    print(f'The year {year} is not included in the list')
