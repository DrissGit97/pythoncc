current_users= ["A1","B2","C3","D4","E5"]
new_users=["A2","B2","C4","D4","E6"]

new_users_lower=[new_user.lower() for new_user in new_users]

for c_user in current_users:
    if c_user.lower() in new_users_lower :
        print(f"Sorry, {c_user} is taken")
    else:
        print(f"This username ({c_user}) is available")