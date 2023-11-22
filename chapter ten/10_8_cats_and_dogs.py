from pathlib import Path

filenames = ["cat_names.txt", "dog_names.txt"]
for filename in filenames:
    print(f"\nReading file {filename}")
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, {path} has not been found.")
    else:
        print(contents)