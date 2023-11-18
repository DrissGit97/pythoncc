people = {
    "person_1" : {
    "f_name" : "name_1", 
    "l_name" : "l_name_1", 
    "age" : "age_1", 
    "city": "city_1"
    },
    "person_2" : {
    "f_name" : "name_2", 
    "l_name" : "l_name_2", 
    "age" : "age_2", 
    "city": "city_2"
    },
    "person_3" : {
    "f_name" : "name_3", 
    "l_name" : "l_name_3", 
    "age" : "age_3", 
    "city": "city_3"
    },
}

for person, person_info in people.items():
    print(f"\nPerson_number: {person}")
    full_name = f"{person_info["f_name"]} {person_info["l_name"]}"
    Age = f"{person_info["age"]}"
    City = f"{person_info["city"]}"

    print(f"\tFull_name: {full_name.title()}")
    print(f"\tAge: {Age}")
    print(f"\tLocation: {City.title()}")