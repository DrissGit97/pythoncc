from pathlib import Path
import json

path = Path("favorite_number_1.json")

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"We remember that your favorite number is {favorite_number}! ;)")
else:
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)

print(f"We'll remember that your favorite number is {favorite_number}!")


