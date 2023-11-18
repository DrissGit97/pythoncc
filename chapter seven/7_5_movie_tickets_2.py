prompt = "If you tell me your age I will tell you how much your movie ticket will cost."
prompt +="\nWhat is your age? "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    age = int(age)
    if age < 3 :
        print("Your ticket is free")
    elif 3 <= age < 12 :
        print("Your ticket is $10")
    elif 12 <= age  :
        print("Your ticket is $15")