from pathlib import Path

path = Path('What is your name.txt')
names = ''

while True:
    print("\nPlease tell me your first and last names.")
    print("(You can quit anytime by typing 'q')")
 
    name = input("First and last names: ")
    if name.lower() == "q":
        break
    names += f"{name}\n"
    
path.write_text(names)