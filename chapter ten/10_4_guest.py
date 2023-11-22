from pathlib import Path

path = Path('What is your name.txt')

while True:
    print("\nPlease tell me your name.")
    print("(You can quit anytime by typing 'q')")
 
    name = input("First and last names: ")
    
    if name.lower() == "q":
        break
    
path.write_text(name)