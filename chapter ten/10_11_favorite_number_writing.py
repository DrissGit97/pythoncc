from pathlib import Path
import json

favorite_number = input("What is your favorite number? ")

path = Path("favorite_number.json")
contents = json.dumps(favorite_number)
path.write_text(contents)

print(f"We'll remember that your favorite number is {favorite_number}!")