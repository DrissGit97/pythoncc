users= ["a1","f2","b3","r5","e4","i8","admin"]

if users:
        for user in users:
            if user=="admin":
                print(f"Hello {user}, would you like to see a status report?")
            else:
                print(f"Hello {user}, thank you for logging in again") 
else:
    print("No users found.")

users= []

if users:
        for user in users:
            if user=="admin":
                print(f"Hello {user}, would you like to see a status report?")
            else:
                print(f"Hello {user}, thank you for logging in again") 
else:
    print("\nNo users found.")