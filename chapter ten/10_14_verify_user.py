from pathlib import Path
import json

path = Path("user_verify")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
#The next part verifies whether the user is yours or not
    user_verification = input (f"Hello! What is your name? ")
    if user_verification.lower() != username.lower():
        other_username = input("\nWhat is your name? (2)")
        contents = json.dumps(other_username)
        path.write_text(contents)
        print(f"We'll remember your name, {other_username} :)")
    else:
        print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you, {username}")