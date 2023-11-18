users= ["a1","f2","b3","r5","e4","i8","admin"]

for user in users:
    if user=="admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again") 