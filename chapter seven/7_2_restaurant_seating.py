nm_people = input("How many customers are you? ")
nm_people = int(nm_people)
if nm_people > 8:
    print("We are currently crowded, please wait a little bit")
else:
    print(f"{nm_people}? Please come in!")