"""Greets user by name, favorite number and age"""

from pathlib import Path
import json

path = Path("userinfo.json")
if path.exists():
    contents = path.read_text()
    user_dict = json.loads(contents)
    print (f"Welcome back, {user_dict['username']}, number {user_dict['fav_number']}, age {user_dict['age']}")
else:
    username = input("What is your name? ")
    fav_number = input("What is your favorite number? ")
    age = input("What is your age? ")

    user_dict = {
        'username' : username,
        'fav_number' : fav_number,
        'age' : age,
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    print (f"We'll remember your user name, {username} :)")
