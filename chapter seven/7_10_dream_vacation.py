#creating an empty list
vacation = {}
#setting a flag to indicate that polling is ctive
polling_active = True
while polling_active:
    #prompt for name and destination
    name = input ("\nWhat is your name?")
    destination = input("And what is your dream vacation? ")

#store responses in a dictionary
    vacation[name] = destination

#Find out if anyone else is going to take the pool.
    repeat = input("Is there anyone left to pool? (yes/no)")
    if repeat.lower() == "no":
        polling_active = False

#Polling is complete
print("\nThe poll has been completed; Here are the results:")
for name, destination in vacation.items():
    print(f"{name.title()} wants to go to {destination.title()}.")